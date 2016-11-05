# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20151109_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Trip Category', max_length=30, null=True)),
                ('short_desc', models.CharField(default=b'Short Decription', max_length=50, null=True)),
                ('long_Desc', models.CharField(default=b'Long Decsription', max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripPlaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Place', max_length=30, null=True)),
                ('desc', models.CharField(default=b'Description', max_length=100, null=True)),
                ('category', models.ForeignKey(to='web.TripCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
