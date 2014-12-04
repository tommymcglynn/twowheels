# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20141121_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='model',
            field=models.ForeignKey(to='web.BikeModel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bikemodel',
            name='family',
            field=models.ForeignKey(to='web.BikeFamily'),
            preserve_default=True,
        ),
    ]
