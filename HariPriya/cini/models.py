from django.db import models
from django.contrib import admin
class Movie(models.Model):
    Genre=models.CharField(max_length=100)
    Name=models.CharField(max_length=20,primary_key=True)
    Director=models.CharField(max_length=100)
    Year=models.IntegerField()
    Music=models.CharField(max_length=100)
 
class MovieAdmin(admin.ModelAdmin):
    list_display=('Genre','Name','Director','Year','Music')