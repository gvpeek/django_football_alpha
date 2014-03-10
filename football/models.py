import json
import sys

from math import ceil
from random import shuffle, random, choice

from django.db import models


class Universe(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=60)

class Year(models.Model):
    def __unicode__(self):
        return unicode(self.year)
        
    year = models.IntegerField(default=1960)
    universe = models.ForeignKey(Universe, related_name='year_universe')
    current_year = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('year','universe')

class Playbook(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=60)
    plays = models.CharField(max_length=10000)

# People

class Player(models.Model):
    
    def __unicode__(self):
        return self.last_name + ', ' + self.first_name
        
    POSITIONS = (
        ('QB', 'Quarterback'),
        ('RB', 'Running Back'),
        ('WR', 'Wide Receiver'),
        ('OT', 'Offensive Tackle'),
        ('OG', 'Offensive Guard'),
        ('C', 'Center'),
        ('DT', 'Defensive Tackle'),
        ('DE', 'Defensive End'),
        ('LB', 'Linebacker'),
        ('CB', 'Corner Back'),
        ('S', 'Safety'),
        ('K', 'Kicker'),
        ('P', 'Punter'),
    )
    
    universe = models.ForeignKey(Universe, related_name='player_universe')
    signed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(default=11)
    position = models.CharField(max_length=2, choices=POSITIONS)
    constitution = models.IntegerField()
    retired = models.BooleanField()
    apex_age = models.IntegerField()
    growth_rate = models.IntegerField()
    declination_rate = models.IntegerField()
    ratings = models.IntegerField() # need to convert to dict

class Coach(models.Model):
    def __unicode__(self):
        return self.last_name + ', ' + self.first_name
    
    universe = models.ForeignKey(Universe, related_name='coach_universe')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    skill = models.IntegerField()
    play_probabilities = models.CharField(max_length=2000)
    fg_dist_probabilities = models.CharField(max_length=1000)

    def practice_plays(self,coach,playbook,skills):
#        results = namedtuple('PracticeResults',['id','runs','success','total_yardage','success_yardage','turnover'])
        play_outcomes = {}
        fg_outcomes = {}
        for play in playbook:
            runs=[]
            success=0
            total_yardage=0
            success_yardage=0
            turnover=0
            if (play.is_rush() or play.is_pass()) and not play.id=='RC':
                for x in range(coach.skill):
                    yds,trn = play.run(skills,{'dl':50,'lb':50,'cb':50,'s':50},0)
                    if trn:
                        turnover += 1
                        yds=-20
                    elif yds > 0:
                        success += 1
                        success_yardage += yds
                    runs.append(yds)
                total_yardage = sum(runs)
                play_outcomes[play.id]={k: (len([i for i in runs if i >= k])/float(len(runs)))*100 for k in range(1,52)}
            elif play.is_field_goal():
                    kicks=[]
                    for x in range((coach.skill / 2)):
                        yds,trn = play.run(skills,{'sp':50},0)
                        kicks.append(yds)
                    max_dist = max(kicks)
                    fg_outcomes={k: (len([i for i in kicks if i >= k])/float(len(kicks)))*100 for k in range(1,61)}
        coach.play_probabilities=json.dumps(play_outcomes)
        coach.fg_dist_probabilities=json.dumps(fg_outcomes)
                        
    def call_play(self,
                  available_plays,
                  state,
                  down_distance,
                  score_difference,
                  period,
                  time_remaining,
                  distance_to_endzone):
        ## 
        ## to sort list of namedtupes: 
        ## in place - list.sort(key=lambda tup: tup.success,reverse=True)
        ## sorted_list = sorted(list, key=lambda tup: tup.success,reverse=True)
        play_choice=None
        target_yards=None
        curr_period,tot_periods=period(True)
        periods_left=tot_periods - curr_period
        if periods_left < 0:
            periods_left=0
        time,period_length=time_remaining(True)
        total_time_remaining= (time.total_seconds() + (periods_left*period_length.total_seconds()))
        if total_time_remaining > 0:
            time_score_ratio=(score_difference()/(total_time_remaining/30.0))
        urgency_threshold=-.4
            
        if state().is_drive():
            down, dist = down_distance()
            if down in [1,2,3] or (down==4 and urgency_threshold > time_score_ratio):
                if urgency_threshold > time_score_ratio:
                    target_yards=ceil(distance_to_endzone()/2)
                elif down in [1,2]:
                    target_yards=ceil(dist/2)
                elif down == 3:
                    target_yards=dist
                play_choice=self.choose_rush_pass_play(available_plays, target_yards)
            elif down == 4:
                try:
                    distance=unicode(int(distance_to_endzone()))
                    if self.fg_dist_probabilities.get(distance) >= 40:
                        play_choice=available_plays['FG']
                except:
                    pass
                if not play_choice:
                    play_choice=available_plays['PUNT']
        elif state().is_conversion():
            if score_difference in [-2,-5,-10,-16,-17,-18] and (urgency_threshold > time_score_ratio or not total_time_remaining):
                play_choice=self.choose_rush_pass_play(available_plays, target_yards)
            else:
                play_choice=available_plays['XP']
        elif state().is_kickoff():
            if urgency_threshold > time_score_ratio:
                play_choice=available_plays['OK']
            else:
                play_choice=available_plays['K']
        elif state().is_free_kick():
            play_choice=available_plays['K']
        
        if not play_choice:
            play_choice = choice(available_plays.values())

        return play_choice
    
    def choose_rush_pass_play(self,
                              available_plays,
                              target_yards):
        target=unicode(int(target_yards))
        play_choice=None
        choices=[]
        success_rates = []
        for play in self.play_probabilities:
            int_play = int(play)

            if int_play in available_plays:
                try:
                    success_rates.append(self.play_probabilities[play].get(target))
                    choices.append(available_plays[int_play])
                except:
                    print 'play call error', sys.exc_info()[0]

        if len(success_rates) and sum(success_rates):
            avg=sum(success_rates)/float(len(success_rates))
            try:
                prob=[((item / avg) /float(len(success_rates))) for item in success_rates]
            except:
                print item, avg, float(len(success_rates)), play, target_yards
            
            r = random()
            running_total=0
            for step in prob:
                # print running_total, r
                if running_total < r < (running_total + step):
                    play_choice = choices[prob.index(step)]
                    print 'play_selected', play_choice
                    break
                running_total += step
                
        return play_choice
 

# Team

class City(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    pro = models.BooleanField() 
    semipro = models.BooleanField()
    amateur = models.BooleanField()
    region = models.IntegerField()
    division = models.IntegerField()
    
class Nickname(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=60)
    pro = models.BooleanField()
    semipro = models.BooleanField()  

def get_draft_position_order():
    order =['QB','RB','WR','OT','OG','C','DT','DE','LB','CB','S','K','P']
    shuffle(order)
    return json.dumps(order)

class Team(models.Model):
    def __unicode__(self):
        return unicode(self.city) + ' ' +unicode(self.nickname)
    
    universe = models.ForeignKey(Universe, related_name='team_universe')
    city = models.ForeignKey(City)
    nickname = models.ForeignKey(Nickname)
    human_control = models.BooleanField(default=False)
    home_field_advantage = models.IntegerField(default=1)
    draft_position_order = models.CharField(max_length=200,
                                     default=get_draft_position_order())
    coach = models.ForeignKey(Coach, related_name='team_coach')
    playbook = models.ForeignKey(Playbook, related_name='team_playbook') 
    primary_color  = models.CommaSeparatedIntegerField(max_length=30)
    secondary_color = models.CommaSeparatedIntegerField(max_length=30)

class Roster(models.Model):
    def __unicode__(self):
        return unicode(self.team) + ' ' + unicode(self.year)
    
    universe = models.ForeignKey(Universe, related_name='roster_universe')    
    team = models.ForeignKey(Team, related_name='roster_team')
    year = models.ForeignKey(Year, related_name='roster_year')
    qb = models.ForeignKey(Player, 
                           related_name='quarterback', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'QB',
                                             'retired' : False})
    rb = models.ForeignKey(Player, 
                           related_name='running back', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'RB',
                                             'retired' : False})
    wr = models.ForeignKey(Player, 
                           related_name='wide receiver', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'WR',
                                             'retired' : False})
    og = models.ForeignKey(Player, 
                           related_name='offensive guard', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'OG',
                                             'retired' : False})
    ot = models.ForeignKey(Player, 
                           related_name='offensive tackle', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'OT',
                                             'retired' : False})
    c = models.ForeignKey(Player, 
                           related_name='center', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'C',
                                             'retired' : False})
    de = models.ForeignKey(Player, 
                           related_name='defensive end', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'DE',
                                             'retired' : False})
    dt = models.ForeignKey(Player, 
                           related_name='defensive tackle', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'DT',
                                             'retired' : False})
    lb = models.ForeignKey(Player, 
                           related_name='linebacker', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'LB',
                                             'retired' : False})
    cb = models.ForeignKey(Player, 
                           related_name='cornerback', 
                           null=True,
                           blank=True,
                           limit_choices_to={'position' : 'CB',
                                             'retired' : False})
    s = models.ForeignKey(Player, 
                          related_name='safety', 
                          null=True,
                          blank=True,
                          limit_choices_to={'position' : 'S',
                                            'retired' : False})
    p = models.ForeignKey(Player, 
                          related_name='punter', 
                          null=True,
                          blank=True,
                          limit_choices_to={'position' : 'P',
                                            'retired' : False})
    k = models.ForeignKey(Player, 
                          related_name='kicker', 
                          null=True,
                          blank=True,
                          limit_choices_to={'position' : 'K',
                                            'retired' : False})
    
    def get_positions(self):
        return ['qb', 'rb', 'wr', 'og', 'c', 'ot', 'dt', 'de', 'lb', 'cb', 's', 'k', 'p']

       
# League                                           
class League(models.Model):
    def __unicode__(self):
        return self.name
        
    LEVELS = (
        ('pro', 'Pro'),
        ('semipro', 'Semi-Pro'),
        ('amateur', 'Amateur'),
    )
    
    universe = models.ForeignKey(Universe, related_name='league_universe')
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=7,choices=LEVELS, default='pro')
    
class LeagueMembership(models.Model):
    def __unicode__(self):
        return unicode(self.league) + ' ' + unicode(self.year)
        
    universe = models.ForeignKey(Universe, related_name='membership_universe')
    year = models.ForeignKey(Year, related_name='membership_year')
    league = models.ForeignKey(League, related_name='membership_league')
    team = models.ForeignKey(Team, related_name='membership_team')
    conference = models.IntegerField()
    division = models.IntegerField()
    
class Game(models.Model):
    def __unicode__(self):
        return unicode(self.away_team) + ' at ' + unicode(self.home_team)
        
    universe = models.ForeignKey(Universe, related_name='game_universe')
    year = models.ForeignKey(Year, related_name='game_year')
    home_team = models.ForeignKey(Team, related_name='game_home_team')
    away_team = models.ForeignKey(Team, related_name='game_away_team')
    number_of_periods = models.IntegerField(default=4)
    use_overtime = models.BooleanField()
    number_of_overtime_periods = models.IntegerField(default=1)
    league_game = models.BooleanField()
    division_game = models.BooleanField()
    conference_game = models.BooleanField()
    playoff_game = models.BooleanField()
    
class Schedule(models.Model):
    def __unicode__(self):
        return unicode(self.week) + ' - ' + unicode(self.game_number) + ' ' + unicode(self.game)
    
    universe = models.ForeignKey(Universe, related_name='schedule_universe')
    year = models.ForeignKey(Year, related_name='schedule_year')
    league = models.ForeignKey(League, related_name='schedule_league')
    game = models.ForeignKey(Game, related_name='schedule_game')
    week = models.IntegerField()
    game_number = models.IntegerField()
    

# Stats

class TeamStats(models.Model):
    def __unicode__(self):
        return unicode(self.team) + ' ' + unicode(self.year)
            
    universe = models.ForeignKey(Universe,related_name='teamstats_universe')
    year = models.ForeignKey(Year, related_name='teamstats_year')
    team = models.ForeignKey(Team, related_name='teamstats_team')
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    score_by_period = models.CommaSeparatedIntegerField(max_length=30, default=[0,0,0,0])
    total_yards = models.IntegerField(default=0)
    pass_att = models.IntegerField(default=0)
    pass_comp = models.IntegerField(default=0)
    completion_pct = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    pass_yards = models.IntegerField(default=0)
    pass_td = models.IntegerField(default=0)
    intercepted = models.IntegerField(default=0)
    sacked = models.IntegerField(default=0)
    rush_att = models.IntegerField(default=0)
    rush_yards = models.IntegerField(default=0)
    rush_td = models.IntegerField(default=0)
    fumbles = models.IntegerField(default=0)
    fg_att = models.IntegerField(default=0)
    fg = models.IntegerField(default=0)
    xp_att = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    conv_att = models.IntegerField(default=0)
    conv = models.IntegerField(default=0)
    punts = models.IntegerField(default=0)
    punt_yards = models.IntegerField(default=0)
    punt_touchbacks = models.IntegerField(default=0)
    punt_blocks = models.IntegerField(default=0)
    punt_returns = models.IntegerField(default=0)
    punt_return_yards = models.IntegerField(default=0)
    kickoffs = models.IntegerField(default=0)
    kickoff_yards = models.IntegerField(default=0)
    kickoff_touchbacks = models.IntegerField(default=0)
    kick_returns = models.IntegerField(default=0)
    kick_return_yards = models.IntegerField(default=0)
    safeties = models.IntegerField(default=0)
    
    def _get_pct(self):
        # calculates winning percentage
        return (self.wins + (self.ties / 2.0)) / (float(self.wins + self.losses + self.ties))
    pct = property(_get_pct)

    # 
    # class Meta:
    #     unique_together = ('year','universe','team')
    
class GameStats(models.Model):
    def __unicode__(self):
        return unicode(self.team) + ' ' + unicode(self.score)
        
    OUTCOMES = (
        ('W', 'Win'),
        ('L', 'Loss'),
        ('T', 'Tie'),
    )
            
    universe = models.ForeignKey(Universe,related_name='gamestats_universe')
    year = models.ForeignKey(Year, related_name='gamestats_year')
    game = models.ForeignKey(Game, related_name='gamestats_game')
    team = models.ForeignKey(Team, related_name='gamestats_team')
    outcome = models.CharField(max_length=1, choices=OUTCOMES)
    score = models.IntegerField(default=0)
    score_by_period = models.CommaSeparatedIntegerField(max_length=30, default=[0,0,0,0])
    total_yards = models.IntegerField(default=0)
    pass_att = models.IntegerField(default=0)
    pass_comp = models.IntegerField(default=0)
    completion_pct = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    pass_yards = models.IntegerField(default=0)
    pass_td = models.IntegerField(default=0)
    intercepted = models.IntegerField(default=0)
    sacked = models.IntegerField(default=0)
    rush_att = models.IntegerField(default=0)
    rush_yards = models.IntegerField(default=0)
    rush_td = models.IntegerField(default=0)
    fumbles = models.IntegerField(default=0)
    fg_att = models.IntegerField(default=0)
    fg = models.IntegerField(default=0)
    xp_att = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    conv_att = models.IntegerField(default=0)
    conv = models.IntegerField(default=0)
    punts = models.IntegerField(default=0)
    punt_yards = models.IntegerField(default=0)
    punt_touchbacks = models.IntegerField(default=0)
    punt_blocks = models.IntegerField(default=0)
    punt_returns = models.IntegerField(default=0)
    punt_return_yards = models.IntegerField(default=0)
    kickoffs = models.IntegerField(default=0)
    kickoff_yards = models.IntegerField(default=0)
    kickoff_touchbacks = models.IntegerField(default=0)
    kick_returns = models.IntegerField(default=0)
    kick_return_yards = models.IntegerField(default=0)
    safeties = models.IntegerField(default=0)
    

    # 
    # class Meta:
    #     unique_together = ('year','universe','game','team')