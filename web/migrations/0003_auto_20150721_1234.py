# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_populate_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='open',
            field=models.BooleanField(default=False, db_column=b'is_open'),
            preserve_default=True,
        ),
    ]
