from django.db import models
from Organizationalunit.models import Organizationalunit

# Create your models here.

class Organizationalchartunit(models.Model):
    cod = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)
    root = models.ForeignKey('Organizationalchartunit', on_delete=models.CASCADE, null=True)
    organizationalunit = models.ForeignKey(Organizationalunit, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cod) + self.name



