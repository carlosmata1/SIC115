# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-21 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161121_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
