# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0002_persona_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='name',
        ),
        migrations.AddField(
            model_name='persona',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='apCasada',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='codUCB',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='documento',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='genero',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='nacionalidad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='primerApellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='segundoApellido',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
