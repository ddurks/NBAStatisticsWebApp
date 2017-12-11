# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView
from django.db.models import Q
from models import NbastatsPlayerinfo, NbastatsSeasonstats, NbastatsTeaminfo
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.yui import LineChart

def home(request):
    context = { 'potential_players' : None }
    return render(request, 'home.html', context)
    
def search(request, searchRequest):
    name = searchRequest.split("-")
    if(len(name)==1 or name[1]==""):
        players = NbastatsPlayerinfo.objects.filter(Q(first_name=name[0].lower()) | Q(last_name=name[0].lower()))
    else:
        players = NbastatsPlayerinfo.objects.filter(first_name=name[0].lower(),last_name=name[1].strip('*').lower())
        if players.count() == 0:
            starname = name[1].lower()+"*"
            players = NbastatsPlayerinfo.objects.filter(first_name=name[0].lower(),last_name=starname)
    
    context = { 'potential_players' : players }
    return render(request, 'home.html', context)

def viewPlayer(request, name, statIn):
    fullname = name.split("-")
    if(len(fullname)==1):
        fullname.add("")
    print fullname[0], fullname[1]
    player = NbastatsPlayerinfo.objects.filter(first_name=fullname[0].lower(),last_name=fullname[1].strip('*').lower())
    if player.count() > 0:
        _player = player[0]
    else:
        starname = fullname[1]+"*"
        player = NbastatsPlayerinfo.objects.filter(first_name=fullname[0],last_name=starname)
        _player = player[0]
    
    stats = _player.nbastatsseasonstats_set.all().order_by("year")
    
    data =  [
            ['Year', 'Stat'],
        ]

    bestSeasonArray = []
    
    for stat in stats:
        PERVAL = ( stat.per * 0.3 )
        PPGVAL = ( stat.pts/stat.g * 0.3 )
        WS = ( stat.ws * 0.3 )
        EFG = stat.efgpct
        RBVAL = ( (stat.trb/stat.g) * 0.2)
        ASTVAL = ( (stat.ast/stat.g) * 0.2)
        STLVAL = ( (stat.stl/stat.g) * 0.1)
        BLKVAL = ( (stat.blk/stat.g) * 0.1)
        TOVVAL = ( (stat.tov/stat.g) * 0.1)
        BESTSEASON = PERVAL + PPGVAL + WS + EFG + RBVAL + ASTVAL + STLVAL + BLKVAL - TOVVAL

        analysis = { 'year': stat.year, 'season': BESTSEASON, }
        bestSeasonArray.append(analysis)

        temp = [stat.year, getattr(stat, statIn)]
        data.append(temp)
        
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = LineChart(data_source)
    # Sort season analysis array by best season
    bestSeasonArray.sort(key=lambda x: x['season'])


    
    context = { 'player' : _player, 'stats' : stats, 'chart' : chart, 'statistic' : statIn, 'bestseason' : bestSeasonArray }

    return render(request, 'player.html', context)



def viewTeam(request, abbrev, yr):
    team = NbastatsTeaminfo.objects.get(abbreviation=abbrev)
    stats = NbastatsSeasonstats.objects.filter(team=abbrev,year=yr)
        
    context = { 'team' : team, 'stats' : stats, 'year' : yr }

    return render(request, 'team.html', context)


def viewAllTeams(request):
    context = { 'teams' : NbastatsTeaminfo.objects.all().order_by("city") }
    return render(request, 'teams.html', context)

def viewAllPlayers(request, letter):
    players = NbastatsPlayerinfo.objects.filter(last_name__startswith=letter).order_by("last_name")
        
    context = { 'players' : players }
    return render(request, 'players.html', context)