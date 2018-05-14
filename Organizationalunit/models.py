from django.db import models

# Create your models here.

class Organizationalunit(models.Model):
    cod = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + self.name



