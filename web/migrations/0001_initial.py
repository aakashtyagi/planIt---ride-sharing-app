# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
import django_countries.fields
import django_extensions.db.fields
import django.utils.timezone
import mb_database.fields
from django.conf import settings
import django_localflavor_us.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveEdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('domain', models.CharField(default=None, max_length=50, null=True)),
                ('url', models.URLField(default=None, max_length=500, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'university',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('id', mb_database.fields.UUIDField(unique=True, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('address_1', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('address_2', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('address_city', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('address_state', django_localflavor_us.models.USStateField(default=None, max_length=2, null=True, blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('address_postal', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('address_country', django_countries.fields.CountryField(default=None, max_length=2, null=True, blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_web_location_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_web_location_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('id', mb_database.fields.UUIDField(unique=True, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('descr', models.TextField(default=None, max_length=1000, null=True, blank=True)),
                ('return_home', models.BooleanField(default=True)),
                ('start_dt', models.DateTimeField(default=None, auto_now_add=True, null=True)),
                ('arrive_dt', models.DateTimeField(default=None, auto_now_add=True, null=True)),
                ('return_dt', models.DateTimeField(default=None, auto_now_add=True, null=True)),
                ('current_members', models.IntegerField(default=0, null=True, blank=True)),
                ('requested_members', models.IntegerField(default=0, null=True, blank=True)),
                ('open', models.BooleanField(default=False)),
                ('arrive_loc', models.ForeignKey(related_name='arriving_locations', default=None, blank=True, to='web.Location', null=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_web_trip_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_web_trip_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
                ('return_loc', models.ForeignKey(related_name='ending_locations', default=None, blank=True, to='web.Location', null=True)),
                ('start_loc', models.ForeignKey(related_name='starting_locations', default=None, blank=True, to='web.Location', null=True)),
            ],
            options={
                'db_table': 'trip',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripParty',
            fields=[
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('id', mb_database.fields.UUIDField(unique=True, serialize=False, editable=False, primary_key=True, blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('gas', models.BooleanField(default=False)),
                ('car', models.BooleanField(default=False)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_web_tripparty_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_web_tripparty_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
                ('trip', models.ForeignKey(related_name='party', default=None, blank=True, to='web.Trip', null=True)),
                ('user', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'trip_member',
            },
            bases=(models.Model,),
        ),
    ]
