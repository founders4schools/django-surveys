from django.conf.urls import url, include
from django.contrib import admin

from surveys.urls import urlpatterns as surveys_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include((surveys_urls, "surveys"), namespace='surveys')),
]
