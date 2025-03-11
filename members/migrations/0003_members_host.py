# Generated by Django 4.2.16 on 2025-03-11 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
        ('members', '0002_alter_members_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='host', to='host.host'),
        ),
    ]
