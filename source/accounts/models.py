from django.db import models
from django.contrib.auth.models import User
from django import forms


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
   
class City(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
      
    class Meta:
        db_table = 'myapp_movie'

City.objects.create(name='Braveheart (1995)'),
City.objects.create(name='Clockwork Orange, A (1971)'),
City.objects.create(name='Dances with Wolves (1990)'),
City.objects.create(name='English Patient, The (1996)'),
City.objects.create(name='Face/Off (1997)'),
City.objects.create(name='Forrest Gump (1994)'),
City.objects.create(name='Game, The (1997)'),
City.objects.create(name='Godfather, The (1972)'),
City.objects.create(name='Jurassic Park (1993)'),
City.objects.create(name='Liar Liar (1997)'),
City.objects.create(name='Lion King, The (1994)'),
City.objects.create(name='Pulp Fiction (1994)'),
City.objects.create(name='Reservoir Dogs (1992)'),
City.objects.create(name='Rock, The (1996)'),
City.objects.create(name='Scream (1996)'),
City.objects.create(name='Seven (Se7en) (1995)'),
City.objects.create(name='Silence of the Lambs, The (1991)'),
City.objects.create(name='Star Trek: First Contact (1996)'),
City.objects.create(name='Star Trek: The Wrath of Khan (1982)'),
City.objects.create(name='Star Wars (1977)'),
City.objects.create(name='Terminator 2: Judgment Day (1991)'),
City.objects.create(name='Titanic (1997)'),
City.objects.create(name='Trainspotting (1996)'),
