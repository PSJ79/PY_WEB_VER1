# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-02 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='modify_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Modeify Date'),
        ),
    ]
