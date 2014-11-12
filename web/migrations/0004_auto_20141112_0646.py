# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_bike_source_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='models',
            field=models.ManyToManyField(related_name='models', to='web.BikeModel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bike',
            name='parts',
            field=models.ManyToManyField(related_name='parts', to='web.BikePart', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bike',
            name='styles',
            field=models.ManyToManyField(related_name='styles', to='web.BikeStyle'),
            preserve_default=True,
        ),
    ]
