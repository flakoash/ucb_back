from django.db import models

# Create your models here.

class Level(models.Model):
    cod = models.CharField(max_length=10)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.cod



