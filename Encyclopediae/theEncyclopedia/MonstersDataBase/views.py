from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import monsters
from .forms import UserFilter

# Create your views here.

#this the view for the home page
def Home(request):
    template = loader.get_template('HomePage.html')
    return HttpResponse(template.render())

#this the view for the list
def search(request):
    Mons_Filter = UserFilter(request.GET, queryset= monsters.objects.all().values())
    template = loader.get_template('MonstersList.html')
    context = {
        'filter': Mons_Filter,
        }
    return HttpResponse(template.render(context, request))

# this is the view for the details of each animals
def details(request, id):
    detailMons = monsters.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'detailMons': detailMons,
    }
    return HttpResponse(template.render(context, request))

