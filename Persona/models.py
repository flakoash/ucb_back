from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name



