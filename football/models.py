import json

from random import shuffle

from django.db import models
# from custom_fields import SeparatedValuesField

# from south.modelsinspector import add_introspection_rules
# add_introspection_rules([], ["^football\.custom_fields\.SeparatedValuesField"])

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
        ('DE', 'Defnesive End'),
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
    # playbook = Playbook()
    # stats = StatBook()
    # coach = Coach()
    # coach.practice_plays(self.playbook,self.skills)
    #     
    # primary_color = (randint(0,255),randint(0,255),randint(0,255))
    # secondary_color = (randint(0,255),randint(0,255),randint(0,255))

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
        return unicode(league.name) + ' ' + unicode(year.year)
        
    universe = models.ForeignKey(Universe, related_name='membership_universe')
    year = models.ForeignKey(Year, related_name='membership_year')
    league = models.ForeignKey(League, related_name='membership_league')
    team = models.ForeignKey(Team, related_name='membership_team')