# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterfaceTest', '0012_result_resultdetail_suite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='input_data',
            field=models.TextField(null=True),
        ),
    ]
