# Generated by Django 4.1.7 on 2023-04-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0006_remove_bikeparking_added_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikeways',
            name='lenght',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
