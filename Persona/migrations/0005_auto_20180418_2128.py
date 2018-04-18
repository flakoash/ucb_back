# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0004_auto_20180418_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apCasada',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
