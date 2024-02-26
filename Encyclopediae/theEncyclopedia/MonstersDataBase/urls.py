from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='home'),
    path('list', views.MonstersJson, name='mons')
]