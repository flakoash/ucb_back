from django.db import models

# Create your models here.

class Unidadorganigrama(models.Model):
    cod = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    dad = models.ForeignKey('Unidadorganigrama', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.cod) + self.name



