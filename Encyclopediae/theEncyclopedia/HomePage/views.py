from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    template = loader.get_template('HomePage.html')
    return HttpResponse(template.render())
