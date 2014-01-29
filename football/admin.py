from django.contrib import admin
from football.models import Player, Year, City, Nickname, Team, Roster, Universe

class TeamAdmin(admin.ModelAdmin):
    list_display = ('city', 'nickname', 'human_control', 'home_field_advantage')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'ratings', 'age', 'retired',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'pro', 'semipro', 'amateur', 'region', 'division')

class NicknameAdmin(admin.ModelAdmin):
    list_display = ('name', 'pro', 'semipro',)
    
class RosterAdmin(admin.ModelAdmin):
    list_display = ('year', 'team', 'qb')
    
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Year)
admin.site.register(City, CityAdmin)
admin.site.register(Nickname, NicknameAdmin)
admin.site.register(Roster, RosterAdmin)
admin.site.register(Universe)
