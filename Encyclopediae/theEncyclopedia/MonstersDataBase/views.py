from django.shortcuts import render
from django.http import JsonResponse
from .models import monsters

# Create your views here.

def MonstersJson(request):
    mons = monsters.objects.all().values()
    monsList = list(mons)
    return JsonResponse(monsList, safe=False)
