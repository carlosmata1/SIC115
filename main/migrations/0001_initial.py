# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-12 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('saldoInicial', models.DecimalField(decimal_places=5, max_digits=5)),
                ('nombre', models.CharField(max_length=50)),
                ('debe', models.DecimalField(decimal_places=5, max_digits=5)),
                ('haber', models.DecimalField(decimal_places=5, max_digits=5)),
                ('saldoFinal', models.DecimalField(decimal_places=5, max_digits=5)),
                ('codigo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nombres', models.TextField(max_length=50)),
                ('apellidos', models.TextField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('direccion', models.TextField(max_length=200)),
                ('telefono', models.CharField(max_length=9)),
                ('contacto', models.CharField(max_length=9)),
                ('dui', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=17)),
                ('afp', models.CharField(max_length=12)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=5, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=200)),
                ('telefono', models.CharField(max_length=9)),
                ('nit', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=30)),
                ('salario', models.DecimalField(decimal_places=5, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTransaccion',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.TextField(max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Empleado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Puesto'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Rubro'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TipoCuenta'),
        ),
    ]
