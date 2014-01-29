from django.db import models

class Universe(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=60)

class Year(models.Model):
    def __unicode__(self):
        return unicode(self.year)
        
    year = models.IntegerField(default=1960)
    universe = models.ForeignKey(Universe, related_name='universe')
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

class Team(models.Model):
    def __unicode__(self):
        return unicode(self.city) + ' ' +unicode(self.nickname)
    
    city = models.ForeignKey(City)
    nickname = models.ForeignKey(Nickname)
    human_control = models.BooleanField(default=False)
    home_field_advantage = models.IntegerField(default=1)
    
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
        
    team = models.ForeignKey(Team)
    year = models.ForeignKey(Year)
    qb = models.ForeignKey(Player, 
                           related_name='quarterback', 
                           limit_choices_to={'position' : 'QB',
                                             'retired' : False})
    rb = models.ForeignKey(Player, 
                           related_name='running back', 
                           limit_choices_to={'position' : 'RB',
                                             'retired' : False})
    wr = models.ForeignKey(Player, 
                           related_name='wide receiver', 
                           limit_choices_to={'position' : 'WR',
                                             'retired' : False})
    og = models.ForeignKey(Player, 
                           related_name='offensive guard', 
                           limit_choices_to={'position' : 'OG',
                                             'retired' : False})
    ot = models.ForeignKey(Player, 
                           related_name='offensive tackle', 
                           limit_choices_to={'position' : 'OT',
                                             'retired' : False})
    de = models.ForeignKey(Player, 
                           related_name='defensive end', 
                           limit_choices_to={'position' : 'DE',
                                             'retired' : False})
    dt = models.ForeignKey(Player, 
                           related_name='defensive tackle', 
                           limit_choices_to={'position' : 'DT',
                                             'retired' : False})
    lb = models.ForeignKey(Player, 
                           related_name='linebacker', 
                           limit_choices_to={'position' : 'LB',
                                             'retired' : False})
    cb = models.ForeignKey(Player, 
                           related_name='cornerback', 
                           limit_choices_to={'position' : 'CB',
                                             'retired' : False})
    s = models.ForeignKey(Player, 
                          related_name='safety', 
                          limit_choices_to={'position' : 'S',
                                            'retired' : False})
    p = models.ForeignKey(Player, 
                          related_name='punter', 
                          limit_choices_to={'position' : 'P',
                                            'retired' : False})
    k = models.ForeignKey(Player, 
                          related_name='kicker', 
                          limit_choices_to={'position' : 'K',
                                            'retired' : False})