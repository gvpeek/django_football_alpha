from django.contrib import admin
from football.models import Player, Year, City, Nickname, Team, Roster, Universe, League, LeagueMembership, Game, Schedule, Coach, Playbook, TeamStats

class YearAdmin(admin.ModelAdmin):
    list_display = ('year', 'current_year', 'universe')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('city', 'nickname', 'human_control', 'home_field_advantage', 'coach', 'draft_position_order', 'universe')

def make_free_agent(modeladmin, request, queryset):
    queryset.update(signed=False)
make_free_agent.short_description = "Make selected players free agents"

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'ratings', 'age', 'signed', 'retired', 'universe',)

    actions = [make_free_agent]

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'pro', 'semipro', 'amateur', 'region', 'division')

class NicknameAdmin(admin.ModelAdmin):
    list_display = ('name', 'pro', 'semipro',)
    
class RosterAdmin(admin.ModelAdmin):
    list_display = ('year', 'team', 'qb', 'rb', 'wr', 'og', 'c', 'ot', 'dt', 'de', 'lb', 'cb', 's', 'k', 'p', 'universe')

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'universe')

class LeagueMembershipAdmin(admin.ModelAdmin):
    list_display = ('league', 'year', 'conference', 'division', 'team', 'universe')

class GameAdmin(admin.ModelAdmin):
    list_display = ('away_team', 'home_team', 'year', 'universe') 

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('week', 'game_number', 'game', 'year', 'league')  
    
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'skill', 'play_probabilities', 'fg_dist_probabilities') 

class PlaybookAdmin(admin.ModelAdmin):
    list_display = ('name', 'plays')

class TeamStatsAdmin(admin.ModelAdmin):
    list_display = ('team', 'year', 'wins', 'losses', 'ties', 'pct', 'score', 'score_by_period', 'total_yards', 'pass_att',  'pass_comp', 'completion_pct', 'pass_yards', 'pass_td',  'intercepted', 'sacked', 'rush_att', 'rush_yards', 'rush_td', 'universe')

admin.site.register(Universe)
admin.site.register(Year, YearAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Nickname, NicknameAdmin)
admin.site.register(Roster, RosterAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(LeagueMembership, LeagueMembershipAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Playbook, PlaybookAdmin)
admin.site.register(TeamStats, TeamStatsAdmin)