'''
Created on Apr 20, 2013

@author: George
'''

from math import ceil
from random import randint, random, choice
from collections import namedtuple

class Coach():
    def __init__(self):
        self.skill = randint(60,90)
        self.play_probabilities = {}
        self.fg_dist_probabilities={}

    def practice_plays(self,playbook,skills):
#        results = namedtuple('PracticeResults',['id','runs','success','total_yardage','success_yardage','turnover'])
        for play in playbook:
            runs=[]
            success=0
            total_yardage=0
            success_yardage=0
            turnover=0
            if (play.is_rush() or play.is_pass()) and not play.id=='RC':
                for x in range(self.skill):
                    yds,trn = play.run(skills,{'dl':50,'lb':50,'cb':50,'s':50},0)
                    if trn:
                        turnover += 1
                        yds=-20
                    elif yds > 0:
                        success += 1
                        success_yardage += yds
                    runs.append(yds)
                total_yardage = sum(runs)
                self.play_probabilities[play.id]={k: (len([i for i in runs if i >= k])/float(len(runs)))*100 for k in range(1,52)}
            elif play.is_field_goal():
                    kicks=[]
                    for x in range((self.skill / 2)):
                        yds,trn = play.run(skills,{'sp':50},0)
                        kicks.append(yds)
                    max_dist = max(kicks)
                    self.fg_dist_probabilities={k: (len([i for i in kicks if i >= k])/float(len(kicks)))*100 for k in range(1,61)}

                        
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
                    if self.fg_dist_probabilities.get(distance_to_endzone()) >= 40:
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
            
#        try:
#            print play_choice.name, score_difference(), period(True), time_remaining().total_seconds(), time_score_ratio, down_distance(), distance_to_endzone()
#        except:
#            pass
        
        return play_choice
    
    def choose_rush_pass_play(self,
                              available_plays,
                              target_yards):
        play_choice=None
        choices=[]
        success_rates = []
        for play in self.play_probabilities:
            if play in available_plays:
                try:
                    success_rates.append(self.play_probabilities[play].get(target_yards))
                    choices.append(available_plays[play])
                except:
                    pass
        if len(success_rates) and sum(success_rates):
            avg=sum(success_rates)/float(len(success_rates))
            try:
                prob=[((item / avg) /float(len(success_rates))) for item in success_rates]
            except:
                print 'Exception', item, avg, float(len(success_rates)), play, target_yards
            
            r = random()
            running_total=0
            for step in prob:
#                print running_total, r
                if running_total < r < (running_total + step):
                    play_choice = choices[prob.index(step)]
                    break
                running_total += step
                
        return play_choice
        
        
        
        
                