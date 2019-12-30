from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    recipes = models.ManyToManyField('Recipe')
    

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


