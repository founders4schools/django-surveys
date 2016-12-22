# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_squashed_0003_auto_20160803_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ratingtype',
            name='name',
            field=models.CharField(choices=[('star-rating', 'Star')], max_length=30, unique=True),
        ),
    ]