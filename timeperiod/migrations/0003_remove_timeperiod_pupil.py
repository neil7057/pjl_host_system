# Generated by Django 4.2.16 on 2025-03-11 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeperiod', '0002_timeperiod_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeperiod',
            name='pupil',
        ),
    ]
