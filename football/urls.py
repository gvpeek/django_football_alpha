from django.conf.urls import patterns, url

from football import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'universe/create/(?P<name>\w+)/$', views.create_universe, name='create_universe'),
    url(r'universe/draft/(?P<universe_id>\d+)/$', views.draft_players, name='draft_players'),

    url(r'playbook/create/$', views.create_playbook, name='create_playbook'),

    url(r'player/(?P<player_id>\d+)/$', views.player, name='player'),
    url(r'player/create/(?P<number>\d+)/$', views.create_players, name='create_players'),
    # url(r'player/age/(?P<years>\d+)/$', views.age_players, name='age_players'),

    url(r'year/advance/(?P<universe_id>\d+)/$', views.advance_year, name='advance_year'),

    url(r'city/initialize/$', views.initialize_cities, name='initialize_cities'),
    url(r'nickname/initialize/$', views.initialize_nicknames, name='initialize_nicknames'),

    url(r'team/create/(?P<level>\w+)/(?P<number>\d+)/$', views.create_teams, name='create_teams'),
    url(r'team/list/(?P<universe_id>\d+)/$', views.show_teams, name='show_teams'),
    url(r'team/roster/(?P<team_id>\d+)/(?P<year>\d+)/$', views.show_roster, name='show_roster'),
    
    url(r'league/create/(?P<universe_id>\d+)/(?P<name>\w+)/(?P<level>\w+)/(?P<nbr_conf>\d+)/(?P<nbr_div>\d+)/(?P<nbr_teams>\d+)/(?P<nbr_playoff_teams>\d+)/$', views.create_league, name='create_league'),    
    url(r'league/standings/(?P<league_id>\d+)/(?P<year>\d+)/$', views.show_standings, name='show_standings'),
    url(r'league/list/(?P<universe_id>\d+)/$', views.show_leagues, name='show_leagues'),
    url(r'league/(?P<league_id>\d+)/$', views.show_league_detail, name='show_league_detail'),
    
)