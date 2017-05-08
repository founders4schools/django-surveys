# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models

from surveys.settings import surveys_settings


class Migration(migrations.Migration):

    replaces = [('surveys', '0001_initial'), ('surveys', '0002_auto_20151218_1000'), ('surveys', '0003_auto_20160803_1427')]

    dependencies = [
        migrations.swappable_dependency(surveys_settings.REVIEWER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RatingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, choices=[('star-rating', 'Star Rating')])),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=50, db_index=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True)),
                ('would_recommend', models.NullBooleanField(default=None)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('rating', models.ForeignKey(related_name='reviews', to='surveys.Rating')),
                ('user', models.ForeignKey(to=surveys_settings.REVIEWER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='type',
            field=models.ForeignKey(related_name='values', to='surveys.RatingType'),
        ),
        migrations.CreateModel(
            name='StarRatedReview',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('surveys.review',),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('object_id', 'content_type', 'user')]),
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['value']},
        ),
    ]
