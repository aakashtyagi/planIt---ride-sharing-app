# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20160209_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripplaces',
            name='alt_tag',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tripplaces',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
