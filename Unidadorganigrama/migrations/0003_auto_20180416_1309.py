# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unidadorganigrama', '0002_auto_20180416_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidadorganigrama',
            name='id',
        ),
        migrations.AlterField(
            model_name='unidadorganigrama',
            name='cod',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
