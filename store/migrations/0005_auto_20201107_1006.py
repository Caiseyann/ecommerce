# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-11-07 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201107_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='profile',
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
