# Generated by Django 4.2.16 on 2025-03-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_remove_members_valid_dbs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='dbs_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
