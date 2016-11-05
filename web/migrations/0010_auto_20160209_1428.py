# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20160209_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripcategory',
            name='pic',
        ),
        migrations.AddField(
            model_name='tripcategory',
            name='alt_tag',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tripcategory',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
