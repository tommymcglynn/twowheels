# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_bike_parts'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='source_url',
            field=models.URLField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
