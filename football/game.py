'''
Created on Mar 1, 2012

@author: George Peek
'''

from math import ceil
from random import choice
from datetime import timedelta
from collections import deque, namedtuple, defaultdict
from time import sleep
#from pprint import pprint

from playbook import Kickoff, Punt, FieldGoal
from state_machine import initialize_state
from stats import StatBook

game_id = 0
global game_id

class Game():
    "Game"
    def __init__(self, 
                 home_team, 
                 away_team, 
                 display=None, 
                 number_of_periods=4,
                 use_overtime=False,
                 number_of_overtime_periods=1, 
                 league_game=False, 
                 division_game=False, 
                 conference_game=False, 
                 playoff_game=False):
        self.id = self.get_next_game_id()
        self.home = home_team
        self.away = away_team
#        self.league_game = league_game
#        self.division_game = division_game
#        self.conference_game = conference_game 
#        self.playoff_game = playoff_game  
        self.number_of_periods = number_of_periods
        self.use_overtime = use_overtime
        self.number_of_overtime_periods = number_of_overtime_periods
        self.period = 1
        self.field = Field(self.get_offense,
                           home_team.primary_color,
                           home_team.secondary_color,
                           away_team.primary_color,
                           away_team.secondary_color)
        self.plays = []
        self.coin_flip_winner = self._coin_flip()
        self._Possession = namedtuple('Possession', ['offense','defense'])
        self.possession = self._possession_setup()
        self.current_state = initialize_state(self.field,
                                   self.change_possession,
                                   self.get_offense)
        self.timekeeping = deque([Clock() for x in range(number_of_periods)])
        self.current_clock = self.timekeeping.pop()
        self.statkeeper = StatKeeper(self.possession,self.number_of_periods)
        self.scoreboard = Scoreboard(self.field,
                                     self.home,
                                     self.away,
                                     self.get_period,
                                     self.get_clock,
                                     self.get_state,
                                     self.get_offense)
        self.end_of_half = False
        self.end_of_regulation = False
        self.in_overtime = False
        self.end_of_game = False
        self.final_processing = False
#        if display:
        self.display = display
#        else:
#            self.display = None
        self.computer_pause = 0
        
    def get_next_game_id(self):
        global game_id
        game_id += 1
        return game_id 
        
    def start_game(self,pause=0):
        self.computer_pause = pause
        if self.display:
            self.display = self.display(self.field,self.scoreboard)
            self.display.update(self.get_display_items())
        ## initial play could have been human input so this wouldn't have been hit yet, so 
        ## we need conditional check
        if not self.end_of_game: 
            self._determine_turn(pause)
        
    def _determine_turn(self,pause):
        if not self.possession.offense.team.human_control:
            sleep(pause)
            play = self.possession.offense.team.coach.call_play(self.get_available_plays(),
                                                                self.get_state,
                                                                self.current_state.get_down_distance,
                                                                self.get_score_difference,
                                                                self.get_period,
                                                                self.current_clock.get_time_remaining,
                                                                self.field.get_distance_to_endzone)
            self.run_play(play)

    def get_display_items(self):
        if self.possession.offense.team.human_control and not self.end_of_game:
            return self.possession.offense.team.human_control, self.end_of_game, self.run_play, self.get_available_plays(), self.field, self.scoreboard
        else:
            return self.possession.offense.team.human_control, self.end_of_game, False,{}, self.field, self.scoreboard
                
                
    def _possession_setup(self):
        PossTeam = namedtuple('PossTeam', ['team','direction','endzone','home_team','plays_run','statbook'])
        
        t1 = PossTeam(self.home,1,0,True,defaultdict(int),StatBook())
        t2 = PossTeam(self.away,-1,100,False,defaultdict(int),StatBook())
        
        # set coin flip loser as initial offense because they will be kicking off
        if self.coin_flip_winner == t1.direction:
            return self._Possession(t2,t1)
        else:
            return self._Possession(t1,t2)

    def _coin_flip(self):
        return choice([-1,1])
        
    def set_second_half(self):
        ## sets up kickoff the opposite of opening kick
        if (self.coin_flip_winner * -1) == self.possession.offense.direction:
            self.change_possession()
            
    def set_overtime(self):
        ## sets up kickoff the opposite of opening kick
        if self.coin_flip_winner == self.possession.offense.direction:
            self.change_possession()
        
    def change_possession(self):
#        print 'chg possession'
        self.possession = self._Possession(self.possession[1],self.possession[0])
        
    def get_offense(self):
        return self.possession.offense

    def get_defense(self):
        return self.possession.defense
    
    def get_home_team(self):
        if self.possession.offense.home_team:
            return self.possession.offense
        else:
            return self.possession.defense

    def get_away_team(self):
        if not self.possession.offense.home_team:
            return self.possession.offense
        else:
            return self.possession.defense
        
    def get_period(self, return_game_length=False):
        if return_game_length:
            return self.period, self.number_of_periods
        else:
            return self.period
    
    def get_state(self):
        return self.current_state
    
    def get_clock(self):
        return self.current_clock
    
    def get_available_plays(self):
        available_plays={}
        for play in self.possession.offense.team.plays:
            if isinstance(self.current_state,(play.valid_states)) and (self.field.get_distance_to_endzone()) > play.valid_yardline:
                available_plays[play.id]=play
        return available_plays
    
    def get_score_difference(self):
        return self.possession.offense.statbook.stats['score'] - self.possession.defense.statbook.stats['score']

    def get_winner(self):
        if self.end_of_game:
                if self.get_home_team().statbook.stats['score'] > self.get_away_team().statbook.stats['score']:
                    return self.get_home_team().team
                elif self.get_home_team().statbook.stats['score'] < self.get_away_team().statbook.stats['score']:
                    return self.get_away_team().team
                else:
                    return None
        else:
            return 'This game has not been completed.'
                
            
    def run_play(self,play_call):
        play = Play(self.possession.offense,
                         self.possession.defense,
                         self.field)
        play.play_call = play_call
        play.run_play()
        self.determine_events(play)
        self.plays.append(play)
        self.statkeeper.update_stats(play,self.get_state)
        if self.current_state.timed_play():
            self.current_clock.run_clock()
        self.current_state = self.current_state.check_state(play.turnover,
                                                            play.events)
        self.check_time_remaining()
        self.scoreboard.refresh(play,self.get_home_team().statbook,self.get_away_team().statbook)
        if self.display:
            self.display.update(self.get_display_items())
        if not self.end_of_game:
            self._determine_turn(self.computer_pause)
        else:
            if not self.final_processing:
                self.compile_stats(self.home.stats.stats, self.get_home_team().statbook.stats)
                self.compile_stats(self.away.stats.stats, self.get_away_team().statbook.stats)
                                    
    def compile_stats(self, team_stats, game_stats):
        for key in team_stats.keys():
            if type(team_stats[key]) is list:
                while len(team_stats[key]) < len(game_stats[key]):
                    team_stats[key].append(0)
                team_stats[key] = [x+y for x,y in zip(team_stats[key],game_stats[key])]
            else:
                team_stats[key] += game_stats[key]
                
        team_stats['completion_pct'] = team_stats['pass_comp'] / team_stats['pass_att']
        
    def check_time_remaining(self):
        if not self.current_clock.get_time_remaining():
            if self.timekeeping:
                if (self.number_of_periods / self.period) == 2:
                    self.end_of_half = True
                self.period += 1
                self.current_clock = self.timekeeping.pop()
            else:
                self.end_of_regulation = True
                if not self.get_score_difference() and self.use_overtime: 
                    if not self.in_overtime:
                        self.in_overtime = True
                        self._coin_flip()
                        self.set_overtime()
                        self.current_state = initialize_state(self.field,
                                                              self.change_possession,
                                                              self.get_offense)
                if self.in_overtime:
#                    print 'in in_overtime'
                    if not self.number_of_overtime_periods or (self.period < (self.number_of_periods + self.number_of_overtime_periods)):
                        self.period += 1
                        self.current_clock = Clock()
                        ## TODO: I don't like doing this here, try to thin kof a better place
                        self.possession[0].statbook.stats['score_by_period'].append(0)
                        self.possession[1].statbook.stats['score_by_period'].append(0)
                    else:
                        self.end_of_game = True
                        self.current_state = None
                        
        if self.end_of_half and self.current_state.timed_play():
            self.set_second_half()
            self.current_state  = initialize_state(self.field,
                                                   self.change_possession,
                                                   self.get_offense)
            self.end_of_half = False
#
        if (self.end_of_regulation and not self.in_overtime and self.current_state.timed_play()) or (self.in_overtime and self.get_score_difference()):                    
            self.end_of_game = True
            self.current_state = None
    
    def determine_events(self,play):
        if play.play_call.is_field_goal():
            play.events['kick_attempt'] = True
#            print 'ayl', (self.field.length - abs(self.field.absolute_yardline - self.possession.offense.endzone)), 'k', play.offense_yardage
            if (self.field.length - abs(self.field.absolute_yardline - self.possession.offense.endzone)) <= play.offense_yardage:
                play.events['kick_successful'] = True
                if self.current_state.is_conversion():
                    self.statkeeper.conversion_kick(self.possession.offense.statbook,self.period)
                elif self.current_state.is_drive():
                    self.statkeeper.field_goal(self.possession.offense.statbook,self.period)
            else:
                play.turnover = True
        else:
            self.field.determine_position(play.offense_yardage * self.possession.offense.direction)
            if not self.field.in_endzone() and play.turnover:
                play.return_yardage = play.play_call.determine_return_yardage(self.possession.defense.team.skills, play.offense_yardage)
                self.field.determine_position(play.return_yardage * self.possession.defense.direction)
            in_endzone = self.field.in_endzone()
            if in_endzone:
                if not in_endzone == self.possession.offense.direction:
                    if self.current_state.is_conversion():
                        play.events['conversion'] = True
                        self.statkeeper.conversion_play(self.possession.offense.statbook,self.period)
                    elif play.turnover:
                        play.events['touchback'] = True
                    else:
                        play.events['offense_touchdown'] = True
                        self.statkeeper.touchdown(self.possession.offense.statbook,self.period)
                else:
                    if play.turnover:
                        play.events['defense_touchdown'] = True
                        self.statkeeper.touchdown(self.possession.defense.statbook,self.period)
                    else:
                        play.events['safety'] = True
                        self.statkeeper.safety(self.possession.defense.statbook,self.period)
                    

class Field():
    "Playing Field"
    def __init__(self, 
                 get_offense,
                 home_ez_prim_color,    
                 home_ez_second_color,                 
                 away_ez_prim_color,    
                 away_ez_second_color,
                 length=100.0,
                 kickoff_yardline=30.0,
                 free_kick_yardline=20.0,
                 conversion_yardline=98.0,
                 touchback_yardline=20.0):
        self.get_offense = get_offense
        self.length = length
        self.kickoff_yardline = kickoff_yardline
        self.free_kick_yardline = free_kick_yardline
        self.conversion_yardline = conversion_yardline
        self.touchback_yardline = touchback_yardline
        self.absolute_yardline = self.kickoff_yardline
        self.converted_yardline = self.kickoff_yardline
        self.home_endzone = 0.0
        self.away_endzone = self.length
        self.endzone_color = {'home_primary' : home_ez_prim_color,
                              'home_secondary' : home_ez_second_color,
                              'away_primary' : away_ez_prim_color,
                              'away_secondary' : away_ez_second_color}
        
        
    def get_distance_to_endzone(self):
        return self.length - abs(self.absolute_yardline - self.get_offense().endzone)
    
    def determine_position(self, yardage):
        self.absolute_yardline += yardage

        if self.absolute_yardline > (self.length / 2):
            self.converted_yardline = self.length - self.absolute_yardline
        else:
            self.converted_yardline = self.absolute_yardline
            
        return self.absolute_yardline

    def in_endzone(self,return_overage=False):
        in_endzone = 0
        overage = 0
        if self.absolute_yardline >= self.away_endzone:
            in_endzone = -1
            overage = self.away_endzone - self.absolute_yardline
        elif self.absolute_yardline <= self.home_endzone:
            in_endzone = 1
            overage = self.home_endzone - self.absolute_yardline
        
        if return_overage:
            return in_endzone, overage
        else:
            return in_endzone

    def _set_ball_position(self,yardline):
        self.absolute_yardline = abs(self.get_offense().endzone - yardline)
        if self.absolute_yardline > self.length / 2:
            self.converted_yardline = abs(self.length - self.absolute_yardline)
        else:
            self.converted_yardline = self.absolute_yardline
                
    def kickoff_set(self):
        self._set_ball_position(self.kickoff_yardline)

    def free_kick_set(self):
        self._set_ball_position(self.free_kick_yardline)
            
    def touchback_set(self):
        self._set_ball_position(self.touchback_yardline)
        
    def conversion_set(self):
        self._set_ball_position(self.conversion_yardline)
        
    def failed_field_goal_set(self):
        self._set_ball_position(self.length - (self.absolute_yardline + (self.get_offense().direction * 7)))
        if self.in_endzone():
            self._set_ball_position(1)
        
class Play():
    def __init__(self,offense,defense,field):
        self.offense = offense
        self.defense = defense
        self.field = field
        self.play_call = None
        self.offense_yardage = 0
        self.return_yardage = 0
        self.turnover = False
        self.events = {'touchback' : False,
                       'punt' : False,
                       'kick_attempt' : False,
                       'kick_successful' : False,
                       'conversion' : False,
                       'safety' : False,
                       'offense_touchdown' : False,
                       'defense_touchdown' : False}
        self.description = ''

    def run_play(self):
        self.offense_yardage, self.turnover = self.play_call.run(self.offense.team.skills,
                                                 self.defense.team.skills,
                                                 self.determine_play_rating_penalty())
     
    def determine_play_rating_penalty(self):
        penalty = 0
        
        if self.play_call.is_rush() or self.play_call.is_pass():
            self.offense.plays_run[self.play_call.id] += 1.0
                
            current_play_ctr = self.offense.plays_run[self.play_call.id]
            total_play_ctr = sum(self.offense.plays_run.values())
        
            play_freq_pct = (current_play_ctr / total_play_ctr)
            if total_play_ctr > 15 and play_freq_pct > .33:
                penalty = ceil((play_freq_pct) * (current_play_ctr * 2.5))
            else:
                penalty = 0
            
            if not self.offense.home_team:
                penalty += self.defense.team.home_field_advantage
    
        return penalty       

class Scoreboard():
    def __init__(self,field,home,away,get_period,get_clock,get_state,get_offense):
        self._field = field
        self.get_period = get_period
        self.get_clock = get_clock
        self.get_state = get_state
        self.get_offense = get_offense
        
        self.scoreboard = {'home_city' : home.city,
                           'home_nickname' : home.nickname,
                           'home_score' : '0',
                           'away_city' : away.city,
                           'away_nickname' : away.nickname,
                           'away_score' : '0',
                           'yardline' : str(int(self._field.converted_yardline)),
                           'period' : str(self.get_period()),
                           'clock' : str(self.get_clock().get_time_remaining())[2:7],
                           'possession' : self.determine_possession(),
                           'description' : ''
                           }
        self.scoreboard['down'], self.scoreboard['yards_to_go'] = self.get_state().get_down_distance(string_format=True)

    def determine_possession(self):
        if self.get_offense().home_team:
            return 'Home'
        else:
            return 'Away'
        
        
    def refresh(self,play,home_stats,away_stats):
        self.scoreboard['home_score'] = str(int((home_stats.stats['score'])))
        self.scoreboard['away_score'] = str(int((away_stats.stats['score'])))
        self.scoreboard['yardline'] = str(int(self._field.converted_yardline))
        self.scoreboard['period'] = str(self.get_period())
        self.scoreboard['clock'] = str(self.get_clock().get_time_remaining())[2:7]
        self.scoreboard['possession'] = self.determine_possession()
        self.scoreboard['description'] = play.description
        print play.description
        # at end of game, state is None, so wrapping in try
        try:
            self.scoreboard['down'], self.scoreboard['yards_to_go'] = self.get_state().get_down_distance(string_format=True)
        except:
            pass

class StatKeeper():
    def __init__(self, teams, periods, touchdown_pts=6, field_goal_pts=3, safety_pts=2, conversion_play_pts=2, conversion_kick_pts=1):        
        teams[0].statbook.stats['score_by_period']=[0 for x in xrange(periods)]
        teams[1].statbook.stats['score_by_period']=[0 for x in xrange(periods)]
        self.touchdown_pts = touchdown_pts
        self.field_goal_pts = field_goal_pts   
        self.safety_pts = safety_pts       
        self.conversion_play_pts = conversion_play_pts
        self.conversion_kick_pts = conversion_kick_pts

    def update_stats(self,play,state):
        endzone, overage = play.field.in_endzone(True)
        if play.play_call.is_kickoff():
            play.offense.statbook.stats['kickoffs'] += 1
            play.offense.statbook.stats['kickoff_yards'] += play.offense_yardage + overage
            play.description = 'Kickoff of {} yards.'.format(str(int(play.offense_yardage)))
            if play.events['touchback']:
                play.offense.statbook.stats['kickoff_touchbacks'] += 1
                play.description += ' Touchback!'
            if play.return_yardage:
                play.defense.statbook.stats['kick_returns'] += 1
                play.defense.statbook.stats['kick_return_yards'] += play.return_yardage + overage
                play.description += ' Returned by {} for {} yards.'.format(play.defense.team.city, str(int(play.return_yardage + overage)))
        elif play.play_call.is_punt():
            play.offense.statbook.stats['punts'] += 1
            play.offense.statbook.stats['punt_yards'] += play.offense_yardage + overage
            if play.offense_yardage == 0:
                play.defense.statbook.stats['punt_blocks'] += 1
                play.description = 'Punt blocked!'
            else:
                play.description = 'Punt of {} yards.'.format(str(int(play.offense_yardage)))
            if play.events['touchback']:
                play.offense.statbook.stats['punt_touchbacks'] += 1
                play.description += ' Touchback!'
            if play.return_yardage:
                play.defense.statbook.stats['punt_returns'] += 1
                play.defense.statbook.stats['punt_return_yards'] += play.return_yardage + overage
                play.description += ' Returned by {} for {} yards.'.format(play.defense.team.city, str(int(play.return_yardage + overage)))
        elif play.play_call.is_field_goal():
            if state().is_conversion():
                play.offense.statbook.stats['xp_att'] += 1
                if play.events['kick_successful']:
                    play.description = 'Extra Point is good!'
                else:
                    play.description = 'Extra Point missed.'
            else:
                play.offense.statbook.stats['fg_att'] += 1
                if play.events['kick_successful']:
                    play.description = '{} yard field goal is good!'.format(str(int(play.field.get_distance_to_endzone() + 7)))
                else:
                    play.description = 'Field goal from {} yards is no good.'.format(str(int(play.field.get_distance_to_endzone())))
        elif state().is_conversion():
            play.offense.statbook.stats['conv_att'] += 1
            if play.offense_yardage > 0:
                play.description = 'Gain of {} yards on the play.'.format(str(int(play.offense_yardage + overage)))
            elif play.offense_yardage < 0:
                play.description = 'Loss of {} yards on the play.'.format(str(-int(play.offense_yardage + overage)))
            else:
                play.description = 'No gain on the play.'
            if play.events['conversion']:
                play.offense.statbook.stats['conv'] += 1
                play.description += ' Conversion successful!'
            else:
                play.description += ' Conversion failed.'
            if play.events['conversion']:
                play.offense.statbook.stats['conv'] += 1
                play.description = ' Conversion successful!'
            else:
                play.description = ' Conversion failed.'
        elif state().is_drive():
            if not play.turnover:
                play.offense.statbook.stats['total_yards'] += play.offense_yardage + overage
                if play.play_call.is_pass():
                    if play.offense_yardage < 0:
                        play.offense.statbook.stats['sacked'] += 1
                        play.description = 'Sacked for a loss of {} yards.'.format(str(int(-play.offense_yardage)))
                    else:
                        play.offense.statbook.stats['pass_att'] += 1
                        if play.offense_yardage > 0:
                            play.offense.statbook.stats['pass_comp'] += 1
                            play.offense.statbook.stats['pass_yards'] += play.offense_yardage + overage
                            play.description = 'Pass complete for {} yards.'.format(str(int(play.offense_yardage + overage)))
                        else:
                            play.description = 'Pass incomplete.'
                        play.offense.statbook.stats['completion_pct'] = play.offense.statbook.stats['pass_comp'] / play.offense.statbook.stats['pass_att']
                    if play.events['offense_touchdown']:
                        play.offense.statbook.stats['pass_td'] += 1
                        play.description += ' Touchdown {}!'.format(play.offense.team.city)
                elif play.play_call.is_rush():
                    play.offense.statbook.stats['rush_att'] += 1
                    play.offense.statbook.stats['rush_yards'] += play.offense_yardage + overage
                    if play.offense_yardage > 0:
                        play.description = 'Run of {} yards.'.format(str(int(play.offense_yardage + overage)))
                    elif play.offense_yardage < 0:
                        play.description = 'Loss of {} yards on the run.'.format(str(-int(play.offense_yardage + overage)))
                    else:
                        play.description = 'No gain on the run.'
                    if play.events['offense_touchdown']:
                        play.offense.statbook.stats['rush_td'] += 1
                        play.description += ' Touchdown {}!'.format(play.offense.team.city)
                if play.events['safety']:
                    play.description += ' Safety!'
            else:
                if play.play_call.is_pass():
                    play.offense.statbook.stats['intercepted'] += 1
                    play.description = 'Pass intercepted by {}! Returned {} yards.'.format(play.defense.team.city,str(int(play.return_yardage)))
                elif play.play_call.is_rush():
                    play.offense.statbook.stats['fumbles'] += 1
                    play.description = 'Fumble! Recovered by {}. Returned {} yards.'.format(play.defense.team.city,str(int(play.return_yardage)))
#        print play.description
   
    def touchdown(self,statbook,period):
        statbook.stats['score'] += self.touchdown_pts
        self.update_period_score(statbook, self.touchdown_pts, period)
        
    def field_goal(self,statbook,period):
        statbook.stats['score'] += self.field_goal_pts
        statbook.stats['fg'] += 1
        self.update_period_score(statbook, self.field_goal_pts, period)

    def safety(self,statbook,period):
        statbook.stats['score'] += self.safety_pts
        statbook.stats['safeties'] += 1
        self.update_period_score(statbook, self.safety_pts, period)

    def conversion_play(self,statbook,period):
        statbook.stats['score'] += self.conversion_play_pts
        statbook.stats['conv'] += 1
        self.update_period_score(statbook, self.conversion_play_pts, period)

    def conversion_kick(self,statbook,period):
        statbook.stats['score'] += self.conversion_kick_pts
        statbook.stats['xp'] += 1
        self.update_period_score(statbook, self.conversion_kick_pts, period)
        
    def update_period_score(self,statbook,score,period):
            statbook.stats['score_by_period'][period-1] += score
        
        
class Clock(object):
    "Basic Clock"
    def __init__(self, quarter_length=15):
        self.quarter_length = quarter_length
        self.time_remaining = timedelta(seconds=(quarter_length*60))

    def get_time_remaining(self,return_qtr_length=False):
        if return_qtr_length:
            return self.time_remaining, timedelta(seconds=(self.quarter_length*60))
        else:
            return self.time_remaining

    def run_clock(self):
        self.time_remaining -= timedelta(seconds=30)
    
        return self.time_remaining
#===============================================================================