# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20160209_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripcategory',
            name='url_name',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
