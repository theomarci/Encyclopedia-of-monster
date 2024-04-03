from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home),
    path('list/', views.MonstersJson),
    path('list/details/<int:id>', views.details),
    path('list/mammals', views.Mammals),
    path('test/', views.feedback_view)
]