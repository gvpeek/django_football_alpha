'''
Created on Apr 14, 2013

@author: George
'''


class StatBook():
    def __init__(self):
        self.stats = {'score' : 0.0,
                      'score_by_period' : [],
                      'total_yards' : 0.0,
                      'pass_att' : 0.0,
                      'pass_comp' : 0.0,
                      'completion_pct' : 0.0,
                      'pass_yards' : 0.0,
                      'pass_td' : 0.0,
                      'intercepted' : 0.0,
                      'sacked' : 0.0,
                      'rush_att' : 0.0,
                      'rush_yards' : 0.0,
                      'rush_td' : 0.0,
                      'fumbles' : 0.0,
                      'fg_att' : 0.0,
                      'fg' : 0.0,
                      'xp_att' : 0.0,
                      'xp' : 0.0,
                      'conv_att' : 0.0,
                      'conv' : 0.0,
                      'punts' : 0.0,
                      'punt_yards' : 0.0,
                      'punt_touchbacks' : 0.0,
                      'punt_blocks' : 0.0,
                      'punt_returns' : 0.0,
                      'punt_return_yards': 0.0,
                      'kickoffs' : 0.0,
                      'kickoff_yards' : 0.0,
                      'kickoff_touchbacks' : 0.0,
                      'kick_returns' : 0.0,
                      'kick_return_yards': 0.0,
                      'safeties': 0.0
                      }