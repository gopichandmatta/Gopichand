from django.db import models


# Create your models here.
class Men(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
