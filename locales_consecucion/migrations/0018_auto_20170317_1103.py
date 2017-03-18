# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locales_consecucion', '0017_auto_20170316_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAulaNotaFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_final', models.FloatField()),
            ],
            options={
                'db_table': 'PersonalAulaNotaFinal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoResultadosCapacitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'TipoResultadoCapacitacion',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='personalaulanotafinal',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.TipoResultadosCapacitacion'),
        ),
        migrations.AddField(
            model_name='personalaulanotafinal',
            name='peaaula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalaula_notafinal', to='locales_consecucion.PersonalAula'),
        ),
    ]
