# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from surveys.admin import ReviewAdmin, RatingAdmin, RatingTypeAdmin
from surveys.models import Review, Rating, RatingType

admin.site.register(RatingType, RatingTypeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)
