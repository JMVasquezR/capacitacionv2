# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
