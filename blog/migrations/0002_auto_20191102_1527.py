# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-02 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now=True, help_text='create date', verbose_name='Create Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, help_text='modify date', verbose_name='Modify Date'),
        ),
    ]