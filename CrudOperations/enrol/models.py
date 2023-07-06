from django.db import models

# Create your models here.

class employees(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=30)
    position=models.CharField(max_length=30)
    salary=models.IntegerField()
    
