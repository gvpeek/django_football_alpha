from django.conf.urls import patterns, url

from football import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'player/(?P<player_id>\d+)/$', views.player, name='player'),
    url(r'player/create/(?P<number>\d+)/$', views.create_players, name='create_players'),
    url(r'player/age/(?P<years>\d+)/$', views.age_players, name='age_players'),

    url(r'year/advance/$', views.advance_year, name='advance_year'),

    url(r'city/initialize/$', views.initialize_cities, name='initialize_cities'),
    url(r'nickname/initialize/$', views.initialize_nicknames, name='initialize_nicknames'),

    url(r'team/create/(?P<level>\w+)/(?P<number>\d+)/$', views.create_teams, name='create_teams'),

)