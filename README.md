# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2025-05-01 191930](https://github.com/user-attachments/assets/63a92452-7e36-40d9-9e66-5900e81da176)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

models.py

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

```


## OUTPUT

![alt text](<Screenshot 2025-03-14 091104.png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
