from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import monsters

# Create your views here.

def Home(request):
    template = loader.get_template('HomePage.html')
    return HttpResponse(template.render())

def MonstersJson(request):
    mons = monsters.objects.all().values()
    template = loader.get_template('MonstersList.html')
    context = {
        'mons': mons,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    detailMons = monsters.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'detailMons': detailMons,
    }
    return HttpResponse(template.render(context, request))

