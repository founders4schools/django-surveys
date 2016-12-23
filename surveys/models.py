# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import, division

import logging

from compat.models import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from .constants import RATING_TYPES_CHOICES
from .managers import ReviewManager, StarRatedReviewManager
from .settings import surveys_settings
from .signals import post_rating

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class RatingType(TimeStampedModel, models.Model):
    name = models.CharField(choices=RATING_TYPES_CHOICES, max_length=30, unique=True)
    min_value = models.IntegerField()
    max_value = models.IntegerField()

    def __str__(self):
        return six.text_type(self.get_name_display())


@python_2_unicode_compatible
class Rating(TimeStampedModel, models.Model):
    value = models.IntegerField(null=True, blank=True)
    type = models.ForeignKey(RatingType, related_name='values', on_delete=models.CASCADE)

    class Meta:
        ordering = ['value']

    def __str__(self):
        plural = 's' if self.value != 1 else ''
        return six.text_type(
            "{0} {1}{2}".format(self.value, self.type, plural).lower()
        )

    def clean(self):
        if self.value is not None:
            if self.value < self.type.min_value or self.value > self.type.max_value:
                msg = _("Invalid Value: should be between {0} and {1}").format(
                    self.type.min_value,
                    self.type.max_value,
                )
                raise ValidationError({'value': msg})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Rating, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Review(TimeStampedModel, models.Model):
    object_id = models.CharField(max_length=50, db_index=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    rating = models.ForeignKey(Rating, related_name='reviews')
    user = models.ForeignKey(surveys_settings.REVIEWER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    would_recommend = models.NullBooleanField(default=None)
    rating_value = None

    objects = ReviewManager()

    class Meta:
        unique_together = [
            ("object_id", "content_type", "user"),
        ]

    def __str__(self):
        return six.text_type("{0} ({1})".format(self.name, self.rating))

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
