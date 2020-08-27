from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    answer = models.CharField(max_length=30)
    choice = models.CharField(max_length=30)

    class Meta:
        db_table = 'Game'
