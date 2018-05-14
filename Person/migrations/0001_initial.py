# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import Person.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codUCB', models.CharField(max_length=10)),
                ('typedocument', models.CharField(max_length=20)),
                ('document', models.CharField(max_length=15)),
                ('issued', models.CharField(max_length=20)),
                ('names', models.CharField(max_length=100)),
                ('firstsurneme', models.CharField(max_length=100)),
                ('secondsurneme', models.CharField(max_length=100)),
                ('mariedsurname', models.CharField(max_length=100, null=True)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(null=True, upload_to=Person.models.user_directory_path)),
                ('phonenumber', models.CharField(max_length=20)),
                ('personalemail', models.CharField(max_length=100)),
                ('ucbemail', models.CharField(max_length=100)),
                ('officephonenumber', models.CharField(max_length=20)),
                ('homeaddress', models.CharField(max_length=200)),
                ('maritalstatus', models.CharField(max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
