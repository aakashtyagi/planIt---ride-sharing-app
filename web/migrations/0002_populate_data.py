from __future__ import unicode_literals
import os
from django.core import serializers
from django.db import models, migrations

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_files = ['menu.json',
                 'admin.json',
                 'site.json',
                 'universities.json',
                 ]


def load_fixture(apps, schema_editor):
    for fixture_file in fixture_files:
        fixture_file = os.path.join(fixture_dir, fixture_file)
        fixture = open(fixture_file, 'rb')
        objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
        for obj in objects:
            obj.save()
        fixture.close()

class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
