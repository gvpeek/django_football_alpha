import os
import csv
import json

from math import floor, pow
from random import choice, randint, shuffle
from copy import deepcopy

from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.template import RequestContext, loader

# import models
from models import Universe, Player, Year, City, Nickname, Team, Roster, get_draft_position_order

import names

def index(request):
    universe_list = Universe.objects.all()
    template = loader.get_template('football/index.html')
    context = RequestContext(request, {
        'universe_list' : universe_list,
    })
    return HttpResponse(template.render(context))
    
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


## Universe 

def create_universe(request, name):
    u = Universe(name=name)
    u.save()
    create_year(request, u, 1945)
    create_teams(request, u, 'pro', 8)
    for x in xrange(30):
        advance_year(request, u)
    Player.objects.filter(universe=u, retired=True).delete()
    draft_players(request,
                  universe_id=u.id)
    
    return HttpResponse("Universe %s created." % name)


## Year
    
def create_year(request, universe, year):
    y = Year(universe=universe,
             year=year)
    y.save()
    
    return HttpResponse("Year %s created." % year)

def advance_year(request,universe):
    y = Year.objects.get(universe=universe,current_year=True)
    y.current_year = False
    y.save()
    new_year = create_year(request, universe, y.year+1)
    age_players(request, universe, 1)
    create_players(request, universe, 600)

    return HttpResponse("Advanced one year.")
    

# Teams

def create_teams(request, universe, level, number):
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
        
    teams = [Team(universe=universe,
                  city=choice(cities),
                  nickname=choice(nicknames),
                  human_control=False,
                  home_field_advantage=randint(1,3),
                  draft_position_order = get_draft_position_order()) for x in xrange(int(number))]
    Team.objects.bulk_create(teams)
    
    return HttpResponse('%s teams created.' % number )
    
def show_teams(request, universe_id):
    u = Universe.objects.get(id=universe_id)
    team_list = Team.objects.filter(universe=u)
    template = loader.get_template('football/team_list.html')
    context = RequestContext(request, {
        'universe' : u,
        'team_list' : team_list,
    })
    return HttpResponse(template.render(context))

def show_roster(request, universe_id, team_id):
    u = Universe.objects.get(id=universe_id)
    y = Year.objects.filter(universe=u, current_year=True)
    t = Team.objects.get(universe=u, id=team_id)
    r = Roster.objects.get(universe=u, team=t, year=y)
    roster = [r.qb, r.rb, r.wr, r.og, r.c, r.ot, r.de, r.dt, r.lb, r.cb, r.s, r.k, r.p]
    template = loader.get_template('football/roster.html')
    context = RequestContext(request, {
        'team' : t,
        'roster' : roster,
    })
    return HttpResponse(template.render(context))
    
def draft_players(request,universe_id):
    u = Universe.objects.get(id=universe_id)
    current_year = Year.objects.get(universe=u,
                                       current_year=True)
    teams = Team.objects.filter(universe=u)
    draft_preference = {}
    nbr_positions = 0 
    for team in teams:
        r = Roster(universe=u,
                   year=current_year,
                   team=team)
        r.save()
        draft_preference[team] = deepcopy(json.loads(team.draft_position_order))
        if not nbr_positions:
            nbr_positions=len(draft_preference[team])
    draft_order=[]
    for i in xrange(nbr_positions):
        for team in teams:
            draft_order.append((team, draft_preference[team][i]))
    for pick in draft_order:
        players = Player.objects.filter(universe=u,
                                        position=pick[1],
                                        retired=False,
                                        signed=False,
                                        age__gte=23).order_by('ratings').reverse()
        p = players[0]
        r = Roster.objects.get(universe=u,
                               year=current_year,
                               team=pick[0])
        print r,pick[1],p
        setattr(r,pick[1].lower(),p)
        r.save()
        p.signed=True
        p.save()
        
    return HttpResponse("Draft for %s in %s complete" % (str(current_year.year), u))

# Players
 
def player(request, player_id):
    player = Player.objects.get(id=player_id)
    
    return HttpResponse("You're looking at player %s - %s %s." % (player_id, player.first_name, player.last_name))

def create_players(request, universe, number):
    players = [Player(universe=universe,
                      first_name=names.first_name(),
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
def age_players(request,universe, years):
    min_max_ratings = [(14,(20,50)), # (age, (min,max))
                        (18,(30,60)),
                        (22,(45,75)),
                        (99,(60,90))]
    for y in xrange(int(years)):
        for player in Player.objects.filter(retired=False,universe=universe):
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

