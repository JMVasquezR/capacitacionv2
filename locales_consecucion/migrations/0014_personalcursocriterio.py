# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locales_consecucion', '0013_personal_id_pea_reemplazo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalCursoCriterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Criterio')),
                ('peaaula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalaula_notas', to='locales_consecucion.PersonalAula')),
            ],
            options={
                'db_table': 'PeaCursoCriterio',
                'managed': True,
            },
        ),
    ]