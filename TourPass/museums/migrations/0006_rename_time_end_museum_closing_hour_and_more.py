# Generated by Django 5.1.4 on 2024-12-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0005_remove_museum_closing_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museum',
            old_name='time_end',
            new_name='closing_hour',
        ),
        migrations.RenameField(
            model_name='museum',
            old_name='time_start',
            new_name='opening_hour',
        ),
    ]