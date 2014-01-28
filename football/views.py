import os
import csv

from math import floor, pow
from random import choice, randint

from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction

from models import Player, Year, City, Nickname, Team

import names

def index(request):
    return HttpResponse("Testing the football index page.")
    
def initialize_cities(request):
    cities = []
    with open(os.path.join('football','csv_source_files','metroareas.csv'), 'r') as cities_file:
        cities_reader = csv.reader(cities_file,delimiter=',')
        for city in cities_reader:
            cities.append(City(name=city[0],
                               state = city[1],
                               pro = bool(int(city[2])),
                               semipro = bool(int(city[3])),
                               amateur = bool(int(city[4])),
                               region = city[5],
                               division = city[6],
                               )
                          )
    City.objects.bulk_create(cities)
    return HttpResponse("Cities inititalized.")

def initialize_nicknames(request):
    nicknames = [] 
    with open(os.path.join('football','csv_source_files','nicknames.csv'), 'r') as nicknames_file:
        nickname_reader = csv.reader(nicknames_file,delimiter=',')
        for nickname in nickname_reader:
            nicknames.append(Nickname(name=nickname[0],
                                      pro = bool(int(nickname[1])),
                                      semipro = bool(int(nickname[2]))
                                      )
                            )
    Nickname.objects.bulk_create(nicknames)
    return HttpResponse("Nicknames inititalized.")    


def create_teams(request, level, number):
    if level == 'any':
        cities = City.objects.all()
        nicknames = Nickname.objects.all()
    elif level in ['pro', 'semipro', 'amateur']:
        level_filter = {}
        level_filter[level] = True
        cities = City.objects.filter(**level_filter)
        nicknames = Nickname.objects.filter(**level_filter)
    else:
        return HttpResponse("Invalid level for team creation.")
        
    teams = [Team(city=choice(cities),
                  nickname=choice(nicknames),
                  human_control=False,
                  home_field_advantage=randint(1,3)) for x in xrange(int(number))]
    Team.objects.bulk_create(teams)
    
    return HttpResponse('%s teams created.' % number )


def player(request, player_id):
    player = Player.objects.get(id=player_id)
    
    return HttpResponse("You're looking at player %s - %s %s." % (player_id, player.first_name, player.last_name))

def create_players(request, number):
    players = [Player(first_name=names.first_name(),
                      last_name=names.last_name(),
                      age = 11,
                      position = choice(['QB','RB','WR','OT','OG','C','DT','DE','LB','CB','S','K','P']),
                      constitution = randint(25,40),
                      retired = False,
                      apex_age = (floor(((32 * 100) * pow(randint(5,100),-.5)) / 100) + 18),
                      growth_rate = randint(1,4),
                      declination_rate = randint(3,5),
                      ratings = randint(25,40)) for x in xrange(int(number))]

    Player.objects.bulk_create(players)

    return HttpResponse("Created %s players." % number)
    
def _check_rating_range(player,range):
    if player.ratings < min(range):
        player.retired = True
    elif player.ratings > max(range):
        player.ratings = max(range)            

@transaction.commit_manually         
def age_players(request,years):
    min_max_ratings = [(14,(20,50)), # (age, (min,max))
                        (18,(30,60)),
                        (22,(45,75)),
                        (99,(60,90))]
    for y in xrange(int(years)):
        for player in Player.objects.filter(retired=False):
            player.age += 1
            if player.age <= player.apex_age:
                player.ratings += randint(1,player.growth_rate)
            else:
                player.ratings -= randint(3,player.declination_rate)
            for age,ratings in min_max_ratings:
                if player.age <= age:
                    _check_rating_range(player, ratings)
                    break
            player.save()
        transaction.commit()
            
    return HttpResponse("Aged players %s years." % years)
    
def advance_year(request):
    y = Year.objects.get(id=1)
    y.year += 1
    y.save()
    age_players(request, 1)
    create_players(request, 75)

    return HttpResponse("Advanced one year.")

            