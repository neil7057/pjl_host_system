# Generated by Django 4.2.16 on 2025-03-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('host', '0004_category_friendly_name_alter_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='host',
            name='categories',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
