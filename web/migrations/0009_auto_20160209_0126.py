# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_tripcategory_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripcategory',
            name='pic',
            field=models.ImageField(default=b'/static/images/world_map.jpg', upload_to=b'static/images/'),
            preserve_default=True,
        ),
    ]
