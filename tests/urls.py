# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django
from django.conf.urls import url, include
from django.contrib import admin

from surveys.urls import urlpatterns as surveys_urls

if django.VERSION < (1, 9):
    admin_urls = include(admin.site.urls)
else:
    admin_urls = admin.site.urls

urlpatterns = [
    url(r'^admin/', admin_urls),
    url(r'^', include(surveys_urls, namespace='surveys')),
]
