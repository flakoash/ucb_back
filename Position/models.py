from django.db import models
from Level.models import Level
from Regional.models import Regional

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.PROTECT)
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



