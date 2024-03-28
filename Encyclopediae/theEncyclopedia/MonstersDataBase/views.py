from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import monsters
from .forms import MyForms

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

def Mammals(request):
    Monsters = monsters.objects.all().values()
    template = loader.get_template("MonstersList.html")
    mons= []
    for i in Monsters:
        value = i.get("monsType")
        if value == "Mammal":
            mons.append(i)
    context = {
        "mons": mons,
    }
    return HttpResponse(template.render(context))

#---------------------------------------------------------------------------------------------TEST---------------------------------------------------------

def test(request):
    template = loader.get_template("test.html")
    return HttpResponse(template.render())

def my_view(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'test.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'test.html', context)
    else:
        form = MyForms()
    context = {
        'form': form
    }
    return render(request, 'test.html', context)
