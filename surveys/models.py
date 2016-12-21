# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import, division

import logging

from compat.models import GenericForeignKey
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .signals import post_rating
from .constants import RATING_TYPES_CHOICES
from .managers import ReviewManager, StarRatedReviewManager

logger = logging.getLogger(__name__)


class RatingType(models.Model):
    name = models.CharField(choices=RATING_TYPES_CHOICES, max_length=30, unique=True)
    min_value = models.IntegerField()
    max_value = models.IntegerField()

    def __unicode__(self):
        return "{0!s}".format(self.name)


class Rating(models.Model):
    value = models.IntegerField(null=True)
    type = models.ForeignKey(RatingType, related_name='values')

    class Meta:
        ordering = ['value']

    def __unicode__(self):
        return "{0!s} {1!s}(s)".format(self.value, self.type.name)

    def clean(self):
        if self.value is not None:
            if self.value < self.type.min_value or self.value > self.type.max_value:
                raise ValidationError({
                    'value': _("Invalid Value: should be between %s and %s") % (self.type.min_value,
                                                                                self.type.min_value)
                })


class Review(models.Model):
    object_id = models.CharField(max_length=50, db_index=True)
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey()
    rating = models.ForeignKey(Rating, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
    would_recommend = models.NullBooleanField(default=None)
    rating_value = None

    objects = ReviewManager()

    class Meta:
        unique_together = [
            ("object_id", "content_type", "user"),
        ]

    def __unicode__(self):
        return "{0!s} ({1!s})".format(self.name, self.rating)

    @property
    def name(self):
        """
        Returns the stored user name.
        """
        if self.user is not None:
            return self.user.get_full_name()

    @property
    def is_negative(self):
        return self.rating.value and (self.rating.value < (self.rating.type.max_value / 2))

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        rated_obj = self.content_object
        signal_kwargs = {
            'sender': rated_obj.__class__,
            'instance': rated_obj,
            'value': self.rating.value,
            'is_negative': self.is_negative,
        }
        logger.debug("Firing signal with: %s", signal_kwargs)
        post_rating.send(**signal_kwargs)


class StarRatedReview(Review):
    objects = StarRatedReviewManager()

    class Meta:
        proxy = True
