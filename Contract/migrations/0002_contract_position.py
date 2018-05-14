# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contract', '0001_initial'),
        ('Position', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='position',
            field=models.ForeignKey(to='Position.Position', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
