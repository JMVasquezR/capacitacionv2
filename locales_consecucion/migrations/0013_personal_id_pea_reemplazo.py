# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locales_consecucion', '0012_auto_20170314_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='id_pea_reemplazo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Personal'),
        ),
    ]