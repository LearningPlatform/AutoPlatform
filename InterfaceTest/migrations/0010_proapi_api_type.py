# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterfaceTest', '0009_proapi_promodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='proapi',
            name='api_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
