from django.db import models


# Create your models here.
class Population(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=30)
    population = models.IntegerField()
    white = models.FloatField()
    black = models.FloatField()
    asian = models.FloatField()
    other = models.FloatField()
    male = models.FloatField()
    female = models.FloatField()
    child = models.FloatField()
    adult = models.FloatField()
    senior = models.FloatField()
