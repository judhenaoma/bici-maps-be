# Generated by Django 4.1.7 on 2023-04-04 15:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0008_rename_description_bikeways_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikeways',
            name='bike_way',
        ),
        migrations.AddField(
            model_name='bikeways',
            name='bike_way_ls',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='bikeways',
            name='bike_way_mls',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='bikeways',
            name='line_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
