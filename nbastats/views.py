# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView
from django.db.models import Q
from models import NbastatsPlayerinfo, NbastatsSeasonstats, NbastatsTeaminfo

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

def viewPlayer(request, name):
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
        
    context = { 'player' : _player, 'stats' : stats }

    return render(request, 'player.html', context)

def viewTeam(request, abbrev, yr):
    team = NbastatsTeaminfo.objects.get(abbreviation=abbrev)
    stats = NbastatsSeasonstats.objects.filter(team=abbrev,year=yr)
        
    context = { 'team' : team, 'stats' : stats, 'year' : yr }

    return render(request, 'team.html', context)


class TeamsView(TemplateView):
    template_name = "teams.html"

class PlayersView(TemplateView):
    template_name = "players.html"