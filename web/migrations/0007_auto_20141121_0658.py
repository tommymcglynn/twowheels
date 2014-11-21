# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20141121_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image_url',
            field=models.URLField(unique=True, max_length=256),
            preserve_default=True,
        ),
    ]
