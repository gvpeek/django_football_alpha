from django.contrib import admin
from football.models import Player, Year, City, Nickname, Team, Roster, Universe,
                            League, LeagueMembership

class YearAdmin(admin.ModelAdmin):
    list_display = ('year', 'current_year', 'universe')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('city', 'nickname', 'human_control', 'home_field_advantage', 'universe')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'ratings', 'age', 'signed', 'retired', 'universe',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'pro', 'semipro', 'amateur', 'region', 'division')

class NicknameAdmin(admin.ModelAdmin):
    list_display = ('name', 'pro', 'semipro',)
    
class RosterAdmin(admin.ModelAdmin):
    list_display = ('year', 'team', 'qb', 'rb', 'wr', 'og', 'c', 'ot', 'dt', 'de', 'lb', 'cb', 's', 'k', 'p', 'universe')

admin.site.register(Universe)
admin.site.register(Year, YearAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Nickname, NicknameAdmin)
admin.site.register(Roster, RosterAdmin)