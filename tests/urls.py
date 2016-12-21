# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from surveys.urls import urlpatterns as surveys_urls

urlpatterns = [
    url(r'^', include(surveys_urls, namespace='surveys')),
]
