"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from nbastats import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^teams/$', views.viewAllTeams),
    url(r'^players/([a-z])$', views.viewAllPlayers),
    url(r'^players/([a-zA-Z]*-[a-zA-Z]*)/stat=([a-zA-Z]*)$', views.viewPlayer),
    url(r'^search=([a-zA-Z]*-[a-zA-Z]*)$', views.search),
    url(r'^teams/([A-Z][A-Z][A-Z])/year=([0-9][0-9][0-9][0-9])$', views.viewTeam),
]
