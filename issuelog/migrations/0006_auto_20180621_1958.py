# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuelog', '0005_auto_20180621_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('bug', 'bug'), ('feature', 'feature')], default='bug', max_length=10),
        ),
    ]
