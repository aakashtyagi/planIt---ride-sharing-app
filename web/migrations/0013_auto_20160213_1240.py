# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_tripcategory_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripcategory',
            name='long_Desc',
            field=models.CharField(default=b'Long Decsription', max_length=500, null=True),
            preserve_default=True,
        ),
    ]
