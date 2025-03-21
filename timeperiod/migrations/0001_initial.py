# Generated by Django 4.2.16 on 2025-03-10 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pupil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeperiod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('pupil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time', to='pupil.pupil')),
            ],
        ),
    ]
