# Generated by Django 4.2.16 on 2025-03-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeperiod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeperiod',
            name='title',
            field=models.CharField(default='timeperiod', max_length=100),
            preserve_default=False,
        ),
    ]
