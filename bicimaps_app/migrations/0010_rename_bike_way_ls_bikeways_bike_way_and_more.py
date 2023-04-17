# Generated by Django 4.1.7 on 2023-04-04 16:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0009_remove_bikeways_bike_way_bikeways_bike_way_ls_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bikeways',
            old_name='bike_way_ls',
            new_name='bike_way',
        ),
        migrations.RemoveField(
            model_name='bikeways',
            name='bike_way_mls',
        ),
        migrations.CreateModel(
            name='BikeWaysMls',
            fields=[
                ('way_id', models.AutoField(primary_key=True, serialize=False)),
                ('bike_way_mls', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('bike_way_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bicimaps_app.bikeways')),
            ],
        ),
    ]