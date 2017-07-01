from django.db import models

# model Food for save menu (name and calories)
class Food(models.Model):
    name = models.CharField(max_length = 200)
    calories = models.IntegerField()
    
    def __str__(self):
       return self.name

# model FoodList for save selected menu 
class FoodList(models.Model):
    name = models.CharField(max_length = 200) # name menu
    number_per_menu = models.IntegerField()   # number(Bowl or plate ) per menu
    calories_per_menu = models.IntegerField() # calories per menu

    def __str__(self):
        return self.name

# model Exercise for save types of exercise and ability to burn
class Exercise(models.Model):
    types = models.CharField(max_length = 200) # types of exercise
    burn = models.IntegerField()               # ability to burn
    
    def __str__(self):
        return self.types

