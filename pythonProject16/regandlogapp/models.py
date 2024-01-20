from django.db import models

# Create your models here.
class Reg(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=8)