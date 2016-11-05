# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20151007_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='arrive_dt',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='return_dt',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_dt',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]
