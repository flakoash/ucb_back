# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Persona.models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0005_auto_20180418_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='photo',
            field=models.ImageField(null=True, upload_to=Persona.models.user_directory_path),
        ),
    ]
