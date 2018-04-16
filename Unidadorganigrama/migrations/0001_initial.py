# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidadorganigrama',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('dad', models.ForeignKey(to='Unidadorganigrama.Unidadorganigrama')),
            ],
        ),
    ]
