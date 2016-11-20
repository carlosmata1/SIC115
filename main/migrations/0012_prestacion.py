# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-17 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20161117_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='prestacion',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('porcentage', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
