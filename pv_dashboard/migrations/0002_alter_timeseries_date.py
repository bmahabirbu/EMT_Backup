# Generated by Django 4.1.5 on 2023-02-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pv_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeseries',
            name='Date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
