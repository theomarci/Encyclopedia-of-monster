from django.db import models

# Create your models here.

class monsters(models.Model):
    # this the variable for each choice when we select the type of animals
    Species = {
        "Mammal": "Mammal",
        "Bird": "Bird",
        "Reptilia": "Reptilia",
        "Fish": "Fish",
        "Arthropoda": "Arthropoda",
    }

    # creation of each fields for the data base about the monsters
    monsName = models.CharField(max_length=200)
    monsScientificName = models.CharField(max_length=200)
    Type = models.CharField(max_length=20, choices=Species)
    monsHigh = models.CharField(max_length=200)
    monsLength = models.CharField(max_length=200)
    monsDiet = models.CharField(max_length=200)
    monsBiome = models.CharField(max_length=200)
    monsSocialBehaviour = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.monsName}"




