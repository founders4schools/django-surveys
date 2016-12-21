# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from .views import AddStarReviewView, QuickCreateStarReviewView

reviews = [
    url(r'^add/(?P<content_type_id>\d+)/(?P<content_id>\w+)$', AddStarReviewView.as_view(), name="reviews_add"),
    url(r'^quick-add/(?P<user_uid>\w+)/(?P<content_type_id>\d+)/(?P<uuid>[\w-]+)$',
        QuickCreateStarReviewView.as_view(), name="quick_add")
]

urlpatterns = [
    url(r'^reviews/', include(reviews, namespace="reviews"))
]
