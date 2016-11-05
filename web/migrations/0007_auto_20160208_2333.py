# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_tripcategory_tripplaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripcategory',
            name='long_Desc',
            field=models.CharField(default=b'Long Decsription', max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tripcategory',
            name='short_desc',
            field=models.CharField(default=b'Short Decription', max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tripcategory',
            name='title',
            field=models.CharField(default=b'Trip Category', max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tripplaces',
            name='desc',
            field=models.CharField(default=b'Description', max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tripplaces',
            name='title',
            field=models.CharField(default=b'Place', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
