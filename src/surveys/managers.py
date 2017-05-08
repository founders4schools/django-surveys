# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.contenttypes.models import ContentType
from django.db import models

from .constants import STAR_RATING_TYPE


class ReviewManager(models.Manager):
    def for_model(self, klass):
        return self.get_queryset().filter(
            content_type=ContentType.objects.get_for_model(klass))

    def for_instance(self, instance):
        return self.get_queryset().filter(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id
        )


class StarRatedReviewManager(ReviewManager):
    def get_queryset(self):
        return super(StarRatedReviewManager, self).get_queryset().filter(rating__type__name=STAR_RATING_TYPE)
