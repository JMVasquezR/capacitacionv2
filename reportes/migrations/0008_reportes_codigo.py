# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0007_reportes_url_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportes',
            name='codigo',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
