# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaSeleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccdd', models.CharField(max_length=2)),
                ('ccpp', models.CharField(max_length=2)),
                ('ccdi', models.CharField(max_length=2)),
                ('ubigeo', models.CharField(max_length=6)),
                ('zona', models.CharField(blank=True, max_length=5, null=True)),
                ('id_convocatoriacargo', models.IntegerField()),
                ('id_cargofuncional', models.IntegerField()),
                ('meta', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'METASELECCION',
            },
        ),
    ]