# Generated by Django 4.1.7 on 2023-05-02 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bicimaps_app', '0017_review_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
