# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubigeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id_ambiente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ambiente', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'AMBIENTE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id_criterio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_criterio', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_criterio', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'CRITERIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('cod_curso', models.CharField(blank=True, max_length=3, null=True)),
                ('nombre_curso', models.CharField(blank=True, max_length=100, null=True)),
                ('nota_minima', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'CURSO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CursoCriterio',
            fields=[
                ('cursocriterio', models.AutoField(primary_key=True, serialize=False)),
                ('ponderacion', models.IntegerField()),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Criterio')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Curso')),
            ],
            options={
                'db_table': 'CURSO_CRITERIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id_etapa', models.AutoField(primary_key=True, serialize=False)),
                ('cod_etapa', models.CharField(blank=True, max_length=3, null=True)),
                ('nombre_etapa', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ETAPA',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_local', models.CharField(blank=True, max_length=300, null=True)),
                ('tipo_via', models.CharField(blank=True, max_length=300, null=True)),
                ('nombre_via', models.CharField(blank=True, max_length=300, null=True)),
                ('referencia', models.CharField(blank=True, max_length=300, null=True)),
                ('n_direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('km_direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('mz_direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('lote_direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('piso_direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('telefono_local_fijo', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono_local_celular', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_inicio', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_fin', models.CharField(blank=True, max_length=100, null=True)),
                ('turno_uso_local', models.CharField(blank=True, max_length=100, null=True)),
                ('capacidad_local_total', models.IntegerField(blank=True, null=True)),
                ('capacidad_local_usar', models.IntegerField(blank=True, null=True)),
                ('funcionario_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('funcionario_email', models.CharField(blank=True, max_length=100, null=True)),
                ('funcionario_cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('funcionario_celular', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable_email', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable_telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable_celular', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad_total_aulas', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_aulas', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_aulas', models.IntegerField(blank=True, null=True)),
                ('cantidad_total_auditorios', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_auditorios', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_auditorios', models.IntegerField(blank=True, null=True)),
                ('cantidad_total_sala', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_sala', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_sala', models.IntegerField(blank=True, null=True)),
                ('cantidad_total_oficina', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_oficina', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_oficina', models.IntegerField(blank=True, null=True)),
                ('cantidad_total_otros', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_otros', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_otros', models.IntegerField(blank=True, null=True)),
                ('especifique_otros', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad_total_computo', models.IntegerField(blank=True, null=True)),
                ('cantidad_disponible_computo', models.IntegerField(blank=True, null=True)),
                ('cantidad_usar_computo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'LOCAL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LocalAmbiente',
            fields=[
                ('id_localambiente', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('n_piso', models.IntegerField(blank=True, null=True)),
                ('capacidad', models.IntegerField(blank=True, null=True)),
                ('id_ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Ambiente')),
                ('id_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Local')),
            ],
            options={
                'db_table': 'LOCAL_AMBIENTE',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='local',
            name='ambientes',
            field=models.ManyToManyField(through='locales_consecucion.LocalAmbiente', to='locales_consecucion.Ambiente'),
        ),
        migrations.AddField(
            model_name='local',
            name='ubigeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubigeo.Ubigeo'),
        ),
        migrations.AddField(
            model_name='local',
            name='zona_ubicacion_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubigeo.Zona'),
        ),
        migrations.AddField(
            model_name='curso',
            name='criterios',
            field=models.ManyToManyField(through='locales_consecucion.CursoCriterio', to='locales_consecucion.Criterio'),
        ),
        migrations.AddField(
            model_name='curso',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales_consecucion.Etapa'),
        ),
        migrations.AlterUniqueTogether(
            name='cursocriterio',
            unique_together=set([('curso', 'cursocriterio')]),
        ),
    ]
