# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locales_consecucion', '0003_personal_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='sexo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
