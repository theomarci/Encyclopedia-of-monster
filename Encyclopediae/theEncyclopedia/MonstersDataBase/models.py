from django.db import models

# Create your models here.

class monsters(models.Model):
    monsName = models.CharField(max_length=200)
    monsScientificName = models.CharField(max_length=200)
    monsType = models.CharField(max_length=200)
    monsHigh = models.CharField(max_length=200)
    monsLength = models.CharField(max_length=200)
    monsWeight = models.CharField(max_length=200)
    monsDiet = models.CharField(max_length=200)
    monsBiome = models.CharField(max_length=200)
    monsSocialBehaviour = models.CharField(max_length=200)
