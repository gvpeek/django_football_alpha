'''
Created on Aug 19, 2012

@author: George Peek
'''

import pprint


#from game import Play
from timekeeping import Clock

def initialize_state(field,change_possession,get_offense,game_params=None):
    return Kickoff(field,change_possession,get_offense)

class State():
    "Basic State"
    def __init__(self,field,change_possession,get_offense,downs_to_convert = 4, yards_to_convert = 10.0):
        self.active = True
        self.field = field
        self.change_possession = change_possession
        self.get_offense = get_offense
        self.downs_to_convert = downs_to_convert
        self.yards_to_convert = yards_to_convert
    
#    def check_state(self):
#        print 'check_state'
#        return Kickoff(self.field,
#                       self.change_possession,
#                       self.get_offense)
    
    def is_kickoff(self):
        return isinstance(self,(Kickoff,FreeKick))
    
    def is_drive(self):
        return isinstance(self,DownSet)
    
    def is_conversion(self):
        return isinstance(self,Conversion)
        
    def timed_play(self):
        return True
    
    def get_down_distance(self,string_format=False):
        if string_format:
            return '',''
        else:
            return 0,0
    
    def check_events(self,events):
        next_state = False
        if events.get('offense_touchdown') or events.get('defense_touchdown'):
            next_state = Conversion(self.field,
                                    self.change_possession,
                                    self.get_offense)
        
        elif events.get('safety'):
            next_state = FreeKick(self.field,
                                 self.change_possession,
                                 self.get_offense)
        
        elif events.get('touchback'):
            self.field.touchback_set()
            next_state = DownSet(self.field,
                                 self.change_possession,
                                 self.get_offense)

        elif events.get('kick_successful'):
            next_state = Kickoff(self.field,
                                 self.change_possession,
                                 self.get_offense)

        elif events.get('kick_attempt'):
            self.field.failed_field_goal_set()
            next_state = DownSet(self.field,
                                 self.change_possession,
                                 self.get_offense)
        
        return next_state




class Kickoff(State):
    "State for kickoffs"
    def __init__(self,*args):
        State.__init__(self,*args)
        self.setup()
        
    def setup(self):
        self.field.kickoff_set()
        
    def check_state(self,turnover,events):
        self.active = False
        if turnover:
            self.change_possession()
        next_state = self.check_events(events)
        if not next_state:
            next_state = DownSet(self.field,
                                 self.change_possession,
                                 self.get_offense)
        
        return next_state

class FreeKick(State):
    "State for free kickoffs"
    def __init__(self,*args):
        State.__init__(self,*args)
        self.setup()
        
    def setup(self):
        self.field.free_kick_set()
        
    def check_state(self,turnover,events):
        self.active = False
        if turnover:
            self.change_possession()
        next_state = self.check_events(events)
        if not next_state:
            next_state = DownSet(self.field,
                                 self.change_possession,
                                 self.get_offense)
        
        return next_state
     
        
class DownSet(State):
    "State for normal offensive possession"
    def __init__(self, *args):
        State.__init__(self,*args)
        self.down = 1
        self.target_yardline = self.field.absolute_yardline + (self.yards_to_convert * self.get_offense().direction) 
        self.converted = False
        self.active = True
        
    def _convert_check(self):
        if not self.active:
            return False
        
        self.yards_to_convert = (self.target_yardline - self.field.absolute_yardline) * self.get_offense().direction
        if (self.yards_to_convert <= 0):
            self.converted = True
            self.active = False
        elif (self.down == 4):
            self.active = False
        else:
            self.down += 1
        
    def check_state(self,turnover,events):
        next_state = False
        if turnover:
            self.active = False
            self.change_possession()
        next_state = self.check_events(events)
        if not next_state:
            self._convert_check()
            if self.converted:
                next_state = DownSet(self.field,
                                     self.change_possession,
                                     self.get_offense)
            else:
                if self.active:
                    next_state = self
                else:
                    if not turnover:
                        self.change_possession()
                    next_state = DownSet(self.field,
                                         self.change_possession,
                                         self.get_offense)
            
        return next_state
    
    def get_down_distance(self,string_format=False):
        if string_format:
            down=str(self.down)
            if self.target_yardline <= 0 or self.target_yardline >= self.field.length:
                distance = 'Goal'
            else:
                distance = str(int(self.yards_to_convert))
        else:
            down=self.down
            if self.target_yardline <= 0 or self.target_yardline >= self.field.length:
                distance=(self.field.length-abs(self.field.absolute_yardline - self.get_offense().endzone))
            else:
                distance = self.yards_to_convert

        return down, distance
        
class Conversion(State):
    "State for conversion attempt after touchdown"
    def __init__(self, *args):
        State.__init__(self,*args)
        self.setup()
        
    def setup(self):
        self.field.conversion_set()        
        
    def timed_play(self):
        return True

    def check_state(self,turnover,events):
        self.active = False
        next_state = Kickoff(self.field,
                             self.change_possession,
                             self.get_offense)
        
        return next_state       