from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Profile/user_{0}/{1}'.format(instance.user.id, filename)


class Person(models.Model):
    codUCB = models.CharField(max_length=10)                  #required
    typedocument = models.CharField(max_length=20, blank=True, null=True)
    document = models.CharField(max_length=15)                #required
    issued = models.CharField(max_length=20, blank=True, null=True)
    names = models.CharField(max_length=100)                    #required
    firstsurneme = models.CharField(max_length=100)             #required
    secondsurneme = models.CharField(max_length=100)            #required
    mariedsurname = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField()                              #required
    gender = models.CharField(max_length=1)                     #required
    nationality = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    personalemail = models.CharField(max_length=100, blank=True, null=True)
    ucbemail = models.CharField(max_length=100, blank=True, null=True)
    officephonenumber = models.CharField(max_length=20, blank=True, null=True)
    homeaddress = models.CharField(max_length=200, blank=True, null=True)
    maritalstatus = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.names + " " + self.firstsurneme

