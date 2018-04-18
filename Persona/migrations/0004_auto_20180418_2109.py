# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0003_auto_20180418_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apCasada',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='codUCB',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacionalidad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primerApellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundoApellido',
            field=models.CharField(max_length=100),
        ),
    ]
