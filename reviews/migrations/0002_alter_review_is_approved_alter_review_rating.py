# Generated by Django 4.2.16 on 2025-03-01 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5, message='Must be between 0-5'), django.core.validators.MinValueValidator(0, message='Must be between 0-5')]),
        ),
    ]
