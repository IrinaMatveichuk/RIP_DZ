# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_shop', '0002_auto_20161208_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='comp_pic',
            field=models.ImageField(blank=True, max_length=1000, upload_to='media/', verbose_name='Фото компьютера'),
        ),
    ]
