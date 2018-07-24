# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-24 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_rudraksh'),
    ]

    operations = [
        migrations.CreateModel(
            name='RudTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moon_sign', models.CharField(default='', max_length=25)),
                ('prescribed', models.CharField(default='', max_length=50)),
                ('prohibited', models.CharField(default='', max_length=25)),
                ('planets', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
