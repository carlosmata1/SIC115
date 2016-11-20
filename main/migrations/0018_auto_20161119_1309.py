# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20161117_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='salario',
            field=models.DecimalField(decimal_places=5, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='salarioNominalDiario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
