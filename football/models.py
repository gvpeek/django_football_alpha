from django.db import models

class Year(models.Model):
    def __unicode__(self):
        return unicode(self.year)
        
    year = models.IntegerField(default=1960)

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

#class Roster(models.Model):
#     team = models.ForeignKey(Team)
#     year = models.ForeignKey(Year)
#     qb = models.ForeignKey(Player)
#     rb = models.ForeignKey(Player)
#     wr = models.ForeignKey(Player)
#     ol = models.ForeignKey(Player)
#     dl = models.ForeignKey(Player)
#     lb = models.ForeignKey(Player)
#     cb = models.ForeignKey(Player)
#     s = models.ForeignKey(Player)
#     p = models.ForeignKey(Player)
#     k = models.ForeignKey(Player)  