from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Persona(models.Model):
    codUCB = models.CharField(max_length=10)
    documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100)
    segundoApellido = models.CharField(max_length=100)
    apCasada = models.CharField(max_length=100, null=True)
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    nacionalidad = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre + " " +self.primerApellido



