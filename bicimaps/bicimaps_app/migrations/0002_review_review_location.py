# Generated by Django 4.1.7 on 2023-03-20 16:23

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
