from django.db import models
from Regional.models import Regional
from Person.models import Person
from Organizationalchartunit.models import Organizationalchartunit
from Position.models import Position
from Performancearea.models import Performancearea
# Create your models here.


class Hireinfo(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Contract(models.Model):
    organizationalchartunit = models.ForeignKey(Organizationalchartunit, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    positiondesc = models.CharField(max_length=200)
    dedication = models.CharField(max_length=200)
    linkage = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    performancearea = models.ForeignKey(Performancearea, on_delete=models.PROTECT)
    hireinfo = models.ForeignKey(Hireinfo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


