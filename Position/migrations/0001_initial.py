# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Regional', '0001_initial'),
        ('Level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.ForeignKey(to='Level.Level', on_delete=django.db.models.deletion.PROTECT)),
                ('regional', models.ForeignKey(to='Regional.Regional', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
    ]
