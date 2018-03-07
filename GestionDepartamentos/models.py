from django.db import models

# Create your models here.

class Regional(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)


    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.nombre + ' - ' + self.sigla

