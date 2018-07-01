# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0003_auto_20180626_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadmap',
            name='content',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='release_num',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Release'),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='releases_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
    ]