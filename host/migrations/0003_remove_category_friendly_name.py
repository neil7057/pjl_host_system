# Generated by Django 4.2.16 on 2025-03-13 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_category_host_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
    ]
