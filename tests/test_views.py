# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status

from surveys.models import StarRatedReview
from .models import Post


class SurveysTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='tintin', password='test')
        self.post = Post.objects.create(author=self.user, title="Welcome", text="Hello World")
        self.content_type = ContentType.objects.get_for_model(Post)
        self.url = reverse('surveys:reviews:reviews_add', args=[self.content_type.id, self.post.id])

    def test_get_url_rate_object(self):
        """Should not be able to run a GET on the rating URL"""
        self.client.login(username='tintin', password='test')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_rate_object_empty(self):
        """When no data is given, the rating should be empty (skipped)"""
        self.client.login(username='tintin', password='test')
        response = self.client.post(self.url)
        self.assertContains(response, '"rating_value":null', status_code=201)
        review = StarRatedReview.objects.first()
        self.assertIsNone(review.rating.value)

    def test_rate_object_data_ok(self):
        """Should be able to only rate an object, without giving any comments"""
        self.client.login(username='tintin', password='test')
        data = {
            'rating_value': 4,
        }
        response = self.client.post(self.url, data=data)
        self.assertContains(response, '"rating_value":4', status_code=201)
        review = StarRatedReview.objects.first()
        self.assertEqual(review.rating.value, 4)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.content_object, self.post)

    def test_rate_object_data_comment(self):
        """When additional info is provided, should be recorded"""
        self.client.login(username='tintin', password='test')
        data = {
            'rating_value': 4,
            'comment': "This was awesome",
            'would_recommend': True,
        }
        response = self.client.post(self.url, data=data)
        self.assertContains(response, '"rating_value":4', status_code=201)
        review = StarRatedReview.objects.first()
        self.assertEqual(review.comment, "This was awesome")
        self.assertTrue(review.would_recommend)

    def test_event_quick_rating(self):
        """If going through quick rating, no need to authenticate"""
        ct = ContentType.objects.get_for_model(self.post)
        url = reverse('surveys:reviews:quick_add', args=['tintin', ct.id, str(self.post.uuid)])
        data = {
            'rating_value': 4,
        }
        response = self.client.post(url, data=data)
        self.assertContains(response, '"rating_value":4', status_code=201)
        review = StarRatedReview.objects.first()
        self.assertEqual(review.rating.value, 4)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.content_object, self.post)
