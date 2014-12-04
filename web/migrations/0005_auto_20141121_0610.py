# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20141112_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BikeMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bikefamily',
            name='make',
            field=models.ForeignKey(to='web.BikeMake'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='bikefamily',
            unique_together=set([('make', 'name')]),
        ),
        migrations.RemoveField(
            model_name='bike',
            name='models',
        ),
        migrations.RemoveField(
            model_name='bikemodel',
            name='type',
        ),
        migrations.AddField(
            model_name='bike',
            name='model',
            field=models.ForeignKey(default=0, to='web.BikeModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bikemodel',
            name='family',
            field=models.ForeignKey(default=0, to='web.BikeFamily'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bikemodel',
            name='name',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='bikemodel',
            unique_together=set([('family', 'name')]),
        ),
    ]
