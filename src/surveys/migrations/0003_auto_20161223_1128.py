# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20161221_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='timestamp',
            field=model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now),
        ),
    ]
