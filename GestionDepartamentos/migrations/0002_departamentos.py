# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDepartamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('sigla', models.CharField(default=b'', max_length=50)),
                ('regional', models.ForeignKey(to='GestionDepartamentos.Regional', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
    ]
