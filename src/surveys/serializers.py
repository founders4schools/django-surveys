# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import logging

from rest_framework import serializers

from .constants import STAR_RATING_TYPE
from .models import Rating, RatingType, StarRatedReview

logger = logging.getLogger(__name__)


class StarRatedReviewSerializer(serializers.ModelSerializer):
    rating_value = serializers.IntegerField(required=False)

    class Meta:
        model = StarRatedReview
        fields = (
            'object_id',
            'content_type',
            'rating_value',
            'comment',
            'would_recommend',
            'user',
        )

    def _get_rating_type(self):
        rating_type, created = RatingType.objects.get_or_create(
            name=STAR_RATING_TYPE, defaults={'min_value': 0, 'max_value': 5})
        logger.info("%s rating type %s", created and "Created new" or "Retrieved existing", rating_type)
        return rating_type

    def _get_rating_obj(self, value):
        rating_type = self._get_rating_type()
        rating, created = Rating.objects.get_or_create(type=rating_type, value=value)
        logger.info("%s rating %s", created and "Created new" or "Retrieved existing", rating)
        return rating

    def to_representation(self, instance):
        data = super(StarRatedReviewSerializer, self).to_representation(instance)
        data['rating_value'] = instance.rating.value
        return data

    def create(self, validated_data):
        logger.info("Calling StarRatedReviewSerializer.create()")
        value = validated_data.pop('rating_value', None)
        validated_data['rating'] = self._get_rating_obj(value)
        return super(StarRatedReviewSerializer, self).create(validated_data)
