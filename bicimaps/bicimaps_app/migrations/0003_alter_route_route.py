# Generated by Django 4.1.7 on 2023-03-21 18:03

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0002_alter_route_review_id_alter_route_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route',
            field=django.contrib.gis.db.models.fields.LineStringField(geography=True, srid=4326),
        ),
    ]
