# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizationalunit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizationalchartunit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod', models.PositiveSmallIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('organizationalunit', models.ForeignKey(to='Organizationalunit.Organizationalunit', on_delete=django.db.models.deletion.PROTECT)),
                ('root', models.ForeignKey(to='Organizationalchartunit.Organizationalchartunit', null=True)),
            ],
        ),
    ]
