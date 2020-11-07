# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-11-07 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201107_0900'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='product_image',
            new_name='category_image',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]