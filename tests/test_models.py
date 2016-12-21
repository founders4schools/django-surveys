# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.test import TestCase

from surveys.constants import STAR_RATING_TYPE
from surveys.models import RatingType, Rating, Review
from .models import Post


class SurveyModelsTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='tintin', first_name='Tintin', password='test')
        self.post = Post.objects.create(author=self.user, title="Welcome", text="Hello World")
        self.rating_type = RatingType.objects.create(name=STAR_RATING_TYPE, min_value=0, max_value=5)
        self.content_type = ContentType.objects.get_for_model(Post)

    def test_rating_type_repr(self):
        self.assertEqual("{0}".format(self.rating_type), "Star")

    def test_rating_repr_1(self):
        rating = Rating.objects.create(type=self.rating_type, value=1)
        self.assertEqual("{0}".format(rating), "1 star")

    def test_rating_repr_4(self):
        rating = Rating.objects.create(type=self.rating_type, value=4)
        self.assertEqual("{0}".format(rating), "4 stars")

    def test_rating_too_high(self):
        r = Rating(type=self.rating_type, value=8)
        self.assertRaises(ValidationError, r.save)

    def test_rating_too_low(self):
        r = Rating(type=self.rating_type, value=-1)
        self.assertRaises(ValidationError, r.save)

    def test_review_repr(self):
        rating = Rating.objects.create(type=self.rating_type, value=4)
        review = Review.objects.create(
            rating=rating, user=self.user, content_type=self.content_type,
            object_id=self.post.id,
        )
        self.assertEqual("{0}".format(review), "Tintin (4 stars)")
