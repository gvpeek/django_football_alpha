import os
import csv
import json
import pickle
import operator

from math import floor, pow
from random import choice, randint, shuffle
from copy import deepcopy
from collections import deque
from ast import literal_eval

from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.template import RequestContext, loader

from game import Game as GameDay
# from coach import Coach # workaround, remove this when fixed
from playbook import Playbook as PlaybookInit # workaround, remove this when fixed
from stats import StatBook # workaround, remove this when fixed

# import models
from models import Universe, Player, Year, City, Nickname, Team, Roster, League, LeagueMembership, get_draft_position_order, Game, Schedule, Coach, Playbook, TeamStats, GameStats

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
        seed_universe_players(u,700)
        create_year(u, 1945)
        # TODO move this to an initialize method
        # TODO investigate better way of testing presence of data
        try:
            Playbook.objects.get(id=1)
        except:
            create_playbook(request)
        try:
            City.objects.get(id=1)
        except:
            initialize_cities(request)
        try:
            Nickname.objects.get(id=1)
        except:
            initialize_nicknames(request)
        create_teams(request, u, 'pro', 8)
        create_league(request, u.id, 'AFL', 'pro', 1, 2, 8, 2)
        
        return HttpResponse("Universe %s created." % name)


## Year
        
def create_year(universe, year):
        y = Year(universe=universe,
                         year=year)
        y.save()
        
        return y

def advance_year(request,universe_id):
        universe = Universe.objects.get(id=universe_id)
        y = Year.objects.get(universe=universe,current_year=True)
        y.current_year = False
        y.save()
        new_year = create_year(universe, y.year+1)
        age_players(universe, 1)
        create_players(request, universe, 600)
        copy_league_memberships(universe, y, new_year)
        copy_rosters(universe, y, new_year)
        draft_players(universe)

        leagues = League.objects.filter(universe=universe)

        for l in leagues:
                create_schedule(l)
                play_season(l)

        return HttpResponse("Advanced one year.")
        
def copy_league_memberships(universe, source_year, new_year):
        current_membership = LeagueMembership.objects.filter(universe=universe, year=source_year)
        for membership in current_membership:
                new_membership = LeagueMembership(universe=membership.universe,
                                                                                    year=new_year,
                                                                                    league=membership.league,
                                                                                    team=membership.team,
                                                                                    conference=membership.conference,
                                                                                    division=membership.division)
                new_membership.save()

def copy_rosters(universe, source_year, new_year):
        current_rosters = Roster.objects.filter(universe=universe, year=source_year)
        for roster in current_rosters:
                roster.id = None
                roster.pk = None
                roster.year = new_year

                for position in roster.get_positions():
                    player = getattr(roster,position)
                    if player.retired:
                        setattr(roster,position,None)
                        setattr(roster,position+'_age',None)
                        setattr(roster,position+'_rating',None)
                    else:
                        setattr(roster,position+'_age',player.age)
                        setattr(roster,position+'_rating',player.ratings)
                roster.save()

# Game

def create_playbook(request):
        p = Playbook(name='Basic',
                                 plays=json.dumps(pickle.dumps(PlaybookInit())))
        p.save()
        
        return HttpResponse("Playbook created")
                

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
                
        coaches = [Coach(universe=universe,
                                        first_name=names.first_name(),
                                        last_name=names.last_name(),
                                        skill=randint(60,90),
                                        play_probabilities = json.dumps({}),
                                        fg_dist_probabilities = json.dumps({})
                                        ) for x in xrange(int(number))]
        for coach in coaches:
                coach.save()
        teams = [Team(universe=universe,
                                    city=choice(cities),
                                    nickname=choice(nicknames),
                                    human_control=False,
                                    home_field_advantage=randint(1,3),
                                    draft_position_order = get_draft_position_order(),
                                    coach = coaches.pop(),
                                    playbook = Playbook.objects.get(id=1)) for x in xrange(int(number))]
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

def show_roster(request, team_id, year):
        t = Team.objects.get(id=team_id)
        y = Year.objects.get(universe=t.universe, year=year)
        r = Roster.objects.get(universe=t.universe, team=t, year=y)
        roster = [r.qb, r.rb, r.wr, r.og, r.c, r.ot, r.de, r.dt, r.lb, r.cb, r.s, r.k, r.p]
        template = loader.get_template('football/roster.html')
        context = RequestContext(request, {
                'team' : t,
                'roster' : roster,
        })
        return HttpResponse(template.render(context)) 

def determine_draft_needs(preference, roster):
        filled=[]
        for position in preference:
                if getattr(roster, position.lower()):
                        filled.append(position)
        for position in filled:
                preference.remove(position)
                preference.append(position)
                
        return preference
     
def draft_players(universe):
        current_year = Year.objects.get(universe=universe,
                                        current_year=True)
        try:
            previous_year = Year.objects.get(universe=universe,
                                             year=(current_year.year - 1))
        except Exception, e:
            print e

        teams=[]
        try:
            team_order=TeamStats.objects.filter(universe=universe,
                                              year=previous_year).order_by('pct')
            for team_stat in team_order:
                teams.append(list(Team.objects.get(id=team_stat.team.id))[0])
        except Exception, e:
            print e

        if not teams:
            teams = Team.objects.filter(universe=universe)
            shuffle(list(teams))
        draft_preference = {}
        nbr_positions = 0 
        for team in teams:
            try:
                r = Roster.objects.get(universe=universe,
                                     year=current_year,
                                     team=team)
            except:
                r = Roster(universe=universe,
                                     year=current_year,
                                     team=team)
                r.save()
            draft_preference[team] = deepcopy(json.loads(team.draft_position_order))
            draft_preference[team] = determine_draft_needs(draft_preference[team], r)
            if nbr_positions < len(draft_preference[team]):
                    nbr_positions=len(draft_preference[team])
        draft_order=[]
        for i in xrange(nbr_positions):
            for team in teams:
                    try:
                            draft_order.append((team, draft_preference[team][i]))
                    except:
                            pass
        for pick_team, pick_position in draft_order:
            players = Player.objects.filter(universe=universe,
                                            position=pick_position,
                                            retired=False,
                                            signed=False,
                                            age__gte=23).order_by('ratings').reverse()
            roster = Roster.objects.get(universe=universe,
                                        year=current_year,
                                        team=pick_team)
            player = players[0]
            current_player = getattr(roster, pick_position.lower())
            if not current_player or \
                    (player.ratings >  current_player.ratings): # and player.age < current_player.age 
                # current_player = Player.objects.get(id=roster.pick_position.lower().id)
                if current_player:
                    current_player.signed=False
                    current_player.save()
                setattr(roster,pick_position.lower(),player)
                setattr(roster,pick_position.lower()+'_age',player.age)
                setattr(roster,pick_position.lower()+'_rating',player.ratings)
                roster.save()
                player.signed=True
                player.save()

        create_coaching_tendencies()
                
        return HttpResponse("Draft for %s in %s complete" % (str(current_year.year), universe))

def create_coaching_tendencies():
        pass

# Players
 
def player(request, player_id):
        player = Player.objects.get(id=player_id)
        
        return HttpResponse("You're looking at player %s - %s %s." % (player_id, player.first_name, player.last_name))

def seed_universe_players(universe, players_per_year):
        def create_player_stub(number):
                players = ['11' + str(randint(25,40)) +
                                                    str(int((floor(((32 * 100) * pow(randint(5,100),-.5)) / 100) + 18))) +
                                                    str(randint(1,4)) +
                                                    str(randint(3,5)) +
                                                    'A' +
                                                    choice(['QB','RB','WR','OT','OG','C','DT','DE','LB','CB','S','K','P'])
                                     for x in xrange(int(number))]

                return players

        def _check_rating_range_stub(rating, rating_range, status):
                if rating < min(rating_range):
                        status = 'R'
                elif rating > max(rating_range):
                        rating = max(rating_range)
                return rating, status

        def age_player_stub(player_data, years=1):
                min_max_ratings = [(14,(20,50)), # (age, (min,max))
                                                        (18,(30,60)),
                                                        (22,(45,75)),
                                                        (99,(60,90))]
                age, rating, apex, inc, dec, status, position = (int(player_data[:2]), 
                                                                                                                int(player_data[2:4]), 
                                                                                                                int(player_data[4:6]),
                                                                                                                int(player_data[6]),
                                                                                                                int(player_data[7]),
                                                                                                                player_data[8],
                                                                                                                player_data[9:])
                for y in xrange(int(years)):        
                        age += 1
                        if age <= apex:
                                rating += randint(1,inc)
                        else:
                                rating -= randint(3,dec)
                        for range_max,ratings in min_max_ratings:
                                if age <= range_max:
                                        rating, status = _check_rating_range_stub(rating, ratings, status)
                                        break
                return str(age)+str(rating)+str(apex)+str(inc)+str(dec)+status+position

        pl=[]
        for x in xrange(50):
                pl = [age_player_stub(player) for player in pl]        
                pl = [player for player in pl if player[8] != 'R']

                pl.extend(create_player_stub(players_per_year))

        players=[]
        for p in pl:
                age, rating, apex, inc, dec, status, position = (int(p[:2]), 
                                                                                                            int(p[2:4]), 
                                                                                                            int(p[4:6]),
                                                                                                            int(p[6]),
                                                                                                            int(p[7]),
                                                                                                            p[8],
                                                                                                            p[9:])
                players.extend([Player(universe=universe,
                                        first_name=names.first_name(),
                                        last_name=names.last_name(),
                                        age = age,
                                        position = position,
                                        constitution = randint(25,40),
                                        retired = False,
                                        apex_age = apex,
                                        growth_rate = inc,
                                        declination_rate = dec,
                                        ratings = rating)])

        Player.objects.bulk_create(players)  

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
                player.signed = False
        elif player.ratings > max(range):
                player.ratings = max(range)
                
@transaction.commit_manually         
def age_players(universe, years):
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

        draft_players(u)        
        create_schedule(l)
        play_season(l)
        
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
                                                                                             use_overtime = True,
                                                                                             league_game = False,
                                                                                             division_game = False,
                                                                                             conference_game = False,
                                                                                             playoff_game = False))
                                        schedule[week+nbr_weeks].append(Game(universe=league.universe,
                                                                                                                 year=y,
                                                                                                                 home_team=rotation2[-1], 
                                                                                                                 away_team=anchor_team,
                                                                                                                 use_overtime = True,
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
        
def play_season(league):
        y = Year.objects.get(universe=league.universe,
                                                 current_year=True)
        schedule = Schedule.objects.filter(universe=league.universe,
                                                                             year=y,
                                                                             league=league)
        for item in schedule:
                g = Game.objects.get(id=item.game.id)
                add_fields_to_team(g.home_team, g)
                add_fields_to_team(g.away_team, g)
                game = GameDay(home_team=g.home_team, 
                                             away_team=g.away_team, 
                                             use_overtime=g.use_overtime)
                game.start_game()
                update_stats(g, game)
                
def add_fields_to_team(team, game):
        roster = Roster.objects.get(universe=game.universe,
                                    year=game.year,
                                    team=team)
        team.skills = {'qb': roster.qb_rating,
                         'rb': roster.rb_rating,
                         'wr': roster.wr_rating,
                         'ol': ((roster.og_rating + roster.c_rating + roster.ot_rating) / 3),
                         'dl': ((roster.dt_rating + roster.de_rating) / 2),
                         'lb': roster.lb_rating,
                         'cb': roster.cb_rating,
                         's': roster.s_rating,
                         'p': roster.p_rating,
                         'k': roster.k_rating,
                         'sp': roster.wr_rating}
        team.primary_color = (randint(0,255),randint(0,255),randint(0,255))
        team.secondary_color = (randint(0,255),randint(0,255),randint(0,255))
        p = Playbook.objects.get(id=1)
        p = json.loads(p.plays)
        p = pickle.loads(p)
        team.plays = p
        team.coach.practice_plays(team.coach,team.plays,team.skills)
        team.coach.save()
        team.coach.play_probabilities = json.loads(team.coach.play_probabilities)
        team.coach.fg_dist_probabilities = json.loads(team.coach.fg_dist_probabilities)
        team.stats = StatBook()

def show_leagues(request, universe_id):
        universe = Universe.objects.get(id=universe_id)
        leagues = League.objects.filter(universe=universe)
        
        template = loader.get_template('football/league_list.html')
        context = RequestContext(request, {
                'universe' : universe.name,
                'league_list' : leagues,
        })
        
        return HttpResponse(template.render(context))

def show_league_detail(request, league_id):
        league = League.objects.get(id=league_id)
        membership_history = LeagueMembership.objects.filter(league=league)
        years = []
        for item in membership_history:
                years.append(item.year)
        
        template = loader.get_template('football/league_detail.html')
        context = RequestContext(request, {
                'league' : league,
                'years' : years,
        })
        
        return HttpResponse(template.render(context))

def show_standings(request, league_id, year):
        l = League.objects.get(id=league_id)
        y = Year.objects.get(universe=l.universe, year=year)
        members = LeagueMembership.objects.filter(universe=l.universe, year=y, league=l).order_by('conference', 'division')
        standings = []
        sorted_standings = []
        for item in members:
                try:
                        standings[item.conference]
                except:
                        standings.append([])
                try:
                        standings[item.conference][item.division]
                except:
                        standings[item.conference].append([])
                stats = TeamStats.objects.get(universe=item.universe, year=item.year, team=item.team)
                standings[item.conference][item.division].append(stats)

        for conference in standings:  
                sorted_standings.append([])
                ix = len(sorted_standings) - 1
                for division in conference:
                        sorted_standings[ix].append(sorted(division, key=operator.attrgetter('pct'), reverse=True))


        schedule_results=[]
        try:
                games = Game.objects.filter(universe=l.universe, year=y)
                for game in games:
                        home_stats = GameStats.objects.get(universe=game.universe,
                                                             year=game.year,
                                                             game=game,
                                                             team=game.home_team)
                        away_stats = GameStats.objects.get(universe=game.universe,
                                                                                             year=game.year,
                                                                                             game=game,
                                                                                             team=game.away_team)
                        away=[]
                        away.extend([away_stats.team])
                        away.extend(literal_eval(away_stats.score_by_period))
                        away.extend([away_stats.score])
                        home=[]
                        home.extend([home_stats.team])
                        home.extend(literal_eval(home_stats.score_by_period))
                        home.extend([home_stats.score])
                        schedule_results.append([away,home])
        except:
                pass

        template = loader.get_template('football/standings.html')
        context = RequestContext(request, {
                'league_name' : l.name,
                'year' : year,
                'standings' : sorted_standings,
                'schedule' : schedule_results,
        })
        return HttpResponse(template.render(context))
        
     
        
# Stats
def get_game_stats(universe, year, game, team):
        try:
                gs = GameStats.objects.get(universe=universe,
                                                                     year=year,
                                                                     game=game,
                                                                     team=team)
        except:
                gs = GameStats(universe=universe,
                                             year=year,
                                             game=game,
                                             team=team)
                gs.save()
        return gs

def get_team_stats(universe, year, team):
        try:
                ts = TeamStats.objects.get(universe=universe,
                                                                     year=year,
                                                                     team=team)
        except:
                ts = TeamStats(universe=universe,
                                             year=year,
                                             team=team)
                ts.save()
        return ts

def update_stats(db_game, game):
        home_db_game_stats = get_game_stats(db_game.universe, db_game.year, db_game, db_game.home_team)
        away_db_game_stats = get_game_stats(db_game.universe, db_game.year, db_game, db_game.away_team)
        home_db_team_stats = get_team_stats(db_game.universe, db_game.year, db_game.home_team)
        away_db_team_stats = get_team_stats(db_game.universe, db_game.year, db_game.away_team)
        home_game_stats = game.get_home_team().statbook.stats
        away_game_stats = game.get_away_team().statbook.stats
        stats = [[home_db_game_stats, home_db_team_stats, home_game_stats],
                         [away_db_game_stats, away_db_team_stats, away_game_stats]]
                         
        if home_game_stats['score'] == away_game_stats['score']:
                home_db_team_stats.ties += 1
                away_db_team_stats.ties += 1
                home_db_game_stats.outcome = 'T'
                away_db_game_stats.outcome = 'T'
        elif home_game_stats['score'] > away_game_stats['score']:
                home_db_team_stats.wins += 1
                away_db_team_stats.losses += 1
                home_db_game_stats.outcome = 'W'
                away_db_game_stats.outcome = 'L'
        else:
                home_db_team_stats.losses += 1
                away_db_team_stats.wins += 1
                home_db_game_stats.outcome = 'L'
                away_db_game_stats.outcome = 'W'

        for db_game_stats, db_team_stats, game_stats in stats:
                for key, game_value in game_stats.iteritems():
                        db_team_value = getattr(db_team_stats,key)
                        ## @TODO fix this to check type
                        if key == 'completion_pct':
                                db_team_value = float(db_team_value)
                        ## @TODO fix this to check type
                        if key == 'score_by_period':
                                db_team_value = literal_eval(db_team_value)
                                while len(db_team_value) < len(game_value):
                                        db_team_value.append(0)
                                db_team_value = [x+y for x,y in zip(db_team_value,game_value)]
                        else:
                                db_team_value += game_value
                        setattr(db_game_stats,key,game_value)
                        setattr(db_team_stats,key,db_team_value)
                db_team_stats.pct = (db_team_stats.wins + (db_team_stats.ties / 2.0)) / (float(db_team_stats.wins + db_team_stats.losses + db_team_stats.ties))
                db_team_stats.completion_pct = (db_team_stats.pass_comp / float(db_team_stats.pass_att))
                db_game_stats.save()
                db_team_stats.save()