# Generated by Django 2.2.28 on 2024-02-29 01:58

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_prueba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
