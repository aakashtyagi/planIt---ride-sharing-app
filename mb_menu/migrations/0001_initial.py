# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mb_database.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', mb_database.fields.UUIDField(unique=True, serialize=False, editable=False, primary_key=True, blank=True)),
                ('item_name', models.CharField(default=None, max_length=50, null=True)),
                ('item_link', models.CharField(default=None, max_length=150, null=True)),
                ('item_created', models.DateTimeField(default=None, auto_now_add=True, null=True)),
                ('item_active', models.BooleanField(default=False)),
                ('item_sort_order', models.IntegerField(default=0, unique=True, null=True, blank=True)),
                ('item_requires_login', models.BooleanField(default=False)),
                ('item_requires_anon', models.BooleanField(default=False)),
                ('item_visible_lg', models.BooleanField(default=True)),
                ('item_visible_md', models.BooleanField(default=True)),
                ('item_visible_sm', models.BooleanField(default=True)),
                ('item_visible_xs', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'MB_FOOTER_LINK',
                'verbose_name': 'Footer Link',
                'verbose_name_plural': 'Footer Links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(default=None, max_length=50, null=True)),
                ('item_link', models.CharField(default=None, max_length=150, null=True)),
                ('item_created', models.DateTimeField(default=None, auto_now_add=True, null=True)),
                ('item_active', models.BooleanField(default=False)),
                ('item_sort_order', models.IntegerField(default=0, null=True, blank=True)),
                ('item_parent', models.IntegerField(default=0, null=True, blank=True)),
                ('item_slug', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('item_requires_login', models.BooleanField(default=False)),
                ('item_requires_anon', models.BooleanField(default=False)),
                ('item_glyph', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('item_visible_lg', models.BooleanField(default=True)),
                ('item_visible_md', models.BooleanField(default=True)),
                ('item_visible_sm', models.BooleanField(default=True)),
                ('item_visible_xs', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'MB_MENU_ITEM',
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
            },
            bases=(models.Model,),
        ),
    ]
