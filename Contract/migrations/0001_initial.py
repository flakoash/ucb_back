# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Regional', '0001_initial'),
        ('Performancearea', '0001_initial'),
        ('Organizationalchartunit', '0001_initial'),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positiondesc', models.CharField(max_length=200)),
                ('dedication', models.CharField(max_length=200)),
                ('linkage', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hireinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('person', models.ForeignKey(to='Person.Person', on_delete=django.db.models.deletion.PROTECT)),
                ('regional', models.ForeignKey(to='Regional.Regional', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='hireinfo',
            field=models.ForeignKey(to='Contract.Hireinfo', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='contract',
            name='organizationalchartunit',
            field=models.ForeignKey(to='Organizationalchartunit.Organizationalchartunit', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='contract',
            name='performancearea',
            field=models.ForeignKey(to='Performancearea.Performancearea', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
