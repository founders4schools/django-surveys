# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20161223_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='timestamp',
            new_name='created',
        ),
    ]
