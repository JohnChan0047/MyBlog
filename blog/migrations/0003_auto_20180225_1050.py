# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-25 10:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180223_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': '关于', 'verbose_name_plural': '关于'},
        ),
        migrations.AddField(
            model_name='about',
            name='about_here',
            field=models.TextField(blank=True, null=True, verbose_name='关于这里'),
        ),
        migrations.AddField(
            model_name='about',
            name='about_me',
            field=models.TextField(blank=True, null=True, verbose_name='关于我'),
        ),
        migrations.AddField(
            model_name='about',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
    ]
