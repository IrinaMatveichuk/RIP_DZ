# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_shop', '0003_auto_20161218_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
