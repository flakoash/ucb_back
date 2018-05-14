from django.db import models

# Create your models here.

class Regional(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=20)

    def __str__(self):
        return self.name



