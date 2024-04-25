from django.urls import path
from . import views

# The different path to the MonstersDataBase app
# For each path, there is the function in views that load the good templates, data.

urlpatterns = [
    path('home/', views.Home),
    path('list/', views.search),
    path('list/details/<int:id>', views.details),
]