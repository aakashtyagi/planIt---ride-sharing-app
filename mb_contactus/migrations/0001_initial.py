# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mb_database.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsQuestion',
            fields=[
                ('id', mb_database.fields.UUIDField(unique=True, serialize=False, editable=False, primary_key=True, blank=True)),
                ('first_name', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('email', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('company', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('question', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
