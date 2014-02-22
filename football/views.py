import os
import csv
import json

from math import floor, pow
from random import choice, randint, shuffle
from copy import deepcopy
from collections import deque

from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.template import RequestContext, loader

from game import Game as GameDay
from coach import Coach # workaround, remove this when fixed
from playbook import Playbook # workaround, remove this when fixed
from stats import StatBook # workaround, remove this when fixed

# import models
from models import Universe, Player, Year, City, Nickname, Team, Roster, League, LeagueMembership, get_draft_position_order, Game, Schedule

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
    create_league(request, u, 'AFL', 'pro', 1, 2, 8, 2)
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


# League

def create_league(request,
                  universe_id,
                  name,
                  level,
                  nbr_conf,
                  nbr_div,
                  nbr_teams,
                  nbr_playoff_teams):
    u = Universe.objects.get(id=universe_id)
    y = Year.objects.get(universe=u,current_year=True)
    universe_teams = Team.objects.filter(universe=u)
    placed_teams = LeagueMembership.objects.filter(universe=u,
                                                   year=y)
    available_teams = set(universe_teams) - set(placed_teams)
    conferences=[]
    for x in xrange(int(nbr_conf)):
        divisions = create_divisions(list(available_teams), int(nbr_div))
        conferences.append(divisions)
    
    l = League(universe=u,
               name=name,
               level=level)
    l.save()
    
    conf_nbr=0
    div_nbr=0
    for conference in conferences:
        for division in divisions:
            for team in division:
                lm = LeagueMembership(universe=u,
                                      year=y,
                                      league=l,
                                      team=team,
                                      conference=conf_nbr,
                                      division=div_nbr)
                lm.save()
            div_nbr+=1
        conf_nbr+=1
        
    create_schedule(l)
    play_season(u,y,l)
    
    return HttpResponse("Created league %s." % name)
                  
def create_divisions(teams,nbr_div):
    divisions=[]
    nbr_teams=len(teams)
    div_size=nbr_teams/nbr_div
    remainder=nbr_teams%nbr_div
    split_start=0
    split_end=0
    for x in xrange(nbr_div):
        split_end += div_size
        if remainder:
            split_end += 1
            remainder -= 1
        divisions.append(teams[split_start:split_end])
        split_start=split_end
    return divisions
    
def create_schedule(league):
    y = Year.objects.get(universe=league.universe,
                         current_year=True)
    teams = LeagueMembership.objects.filter(universe=league.universe,
                                            year=y,
                                            league=league)
    structure = {}
    for team in teams:
        structure.setdefault(team.conference, {})
        structure[team.conference].setdefault(team.division, [])
        structure[team.conference][team.division].append(team.team)
    schedule = []
    for conference, divisions in structure.iteritems():
        for div_nbr, division in divisions.iteritems():
            anchor_team = None
            # 'balanced' will contain 1 if even number of teams,, 0 if odd
            # used later to calculate number of weeks needed, since odd
            # numbered divisions require an extra week due to each team having a bye
            balanced = 1 - (len(division) % 2)
            nbr_weeks = len(division) - balanced
            max_weeks = 2 * nbr_weeks
            try:
                schedule[max_weeks]
            except:
                for x in xrange(max_weeks - len(schedule)):
                    schedule.append([])
            ## gpw is games per week
            gpw = len(division) / 2
            rotation1 = deque(division[:gpw])
            rotation2 = deque(division[gpw:])
            if balanced:
                anchor_team = rotation1.popleft()
            for week in range(nbr_weeks):
                if anchor_team:
                    schedule[week].append(Game(universe=league.universe,
                                               year=y,
                                               home_team=anchor_team, 
                                               away_team=rotation2[-1],
                                               use_overtime = False,
                                               league_game = False,
                                               division_game = False,
                                               conference_game = False,
                                               playoff_game = False))
                    schedule[week+nbr_weeks].append(Game(universe=league.universe,
                                                         year=y,
                                                         home_team=rotation2[-1], 
                                                         away_team=anchor_team,
                                                         use_overtime = False,
                                                         league_game = False,
                                                         division_game = False,
                                                         conference_game = False,
                                                         playoff_game = False))
                for t1, t2 in zip(rotation1,rotation2):
                    schedule[week].append(Game(universe=league.universe,
                                               year=y,
                                               home_team=t1,
                                               away_team=t2,
                                               use_overtime = False,
                                               league_game = False,
                                               division_game = False,
                                               conference_game = False,
                                               playoff_game = False))
                    schedule[week+nbr_weeks].append(Game(universe=league.universe,
                                                         year=y,
                                                         home_team=t2,
                                                         away_team=t1,
                                                         use_overtime = False,
                                                         league_game = False,
                                                         division_game = False,
                                                         conference_game = False,
                                                         playoff_game = False))

                rotation1.append(rotation2.pop())
                rotation2.appendleft(rotation1.popleft())

        for week in schedule:
            for game in week:
                game.save()
                s = Schedule(universe=league.universe,
                                               year=y,
                                               league=league,
                                               game=game,
                                               week=schedule.index(week) + 1,
                                               game_number=week.index(game) + 1)
                s.save()
    
def play_season(universe,year,league):
    schedule = Schedule.objects.filter(universe=universe,
                                       year=year,
                                       league=league)
    for item in schedule:
        g = Game.objects.get(id=item.game.id)
        add_fields_to_team(g.home_team, g)
        add_fields_to_team(g.away_team, g)
        game = GameDay(g.home_team, g.away_team)
        game.start_game()
        print game.get_away_team().team.city, game.get_away_team().statbook.stats['score_by_period'], game.get_away_team().statbook.stats['score']
        print game.get_home_team().team.city, game.get_home_team().statbook.stats['score_by_period'], game.get_home_team().statbook.stats['score']
        print
        
def add_fields_to_team(team, game):
    roster = Roster.objects.get(universe=game.universe,
                                     year=game.year,
                                     team=team)
    team.skills = {'qb': roster.qb.ratings,
                   'rb': roster.rb.ratings,
                   'wr': roster.wr.ratings,
                   'ol': ((roster.og.ratings + roster.c.ratings + roster.ot.ratings) / 3),
                   'dl': ((roster.dt.ratings + roster.de.ratings) / 2),
                   'lb': roster.lb.ratings,
                   'cb': roster.cb.ratings,
                   's': roster.s.ratings,
                   'p': roster.p.ratings,
                   'k': roster.k.ratings,
                   'sp': roster.wr.ratings}
    team.primary_color = (randint(0,255),randint(0,255),randint(0,255))
    team.secondary_color = (randint(0,255),randint(0,255),randint(0,255))
    team.coach = Coach()
    team.playbook = Playbook()
    team.stats = StatBook()