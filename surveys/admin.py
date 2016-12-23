# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .constants import STAR_RATING_TYPE
from .models import RatingType, Rating, Review
from .settings import surveys_settings


@admin.register(RatingType)
class RatingTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_value', 'max_value')
    search_fields = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('value', 'type')
    list_filter = ('type',)


class BadRatingFilter(admin.SimpleListFilter):
    title = "Bad Reviews"
    parameter_name = 'bad_reviews'

    def lookups(self, request, model_admin):
        return [
            ('y', "Below 3 stars"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'y':
            return queryset.filter(rating__value__lt=3)
        return queryset


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_for',
        'item_type',
        'rating_value',
        'user',
        'created',
        'comment',
        'would_recommend',
    )
    list_filter = (
        BadRatingFilter,
        ('content_type', admin.RelatedOnlyFieldListFilter),
        ('rating', admin.RelatedOnlyFieldListFilter),
        'created',
    )
    search_fields = ('user__first_name', 'user__last_name', 'comment')

    @property
    def media(self):
        media = super(ReviewAdmin, self).media
        fa_css = surveys_settings.FONT_AWESOME_CSS
        media.add_css({'all': (fa_css,)} if fa_css else {})
        return media

    def item_type(self, obj):
        return "{0}".format(obj.content_type).capitalize()

    def review_for(self, obj):
        return "{0}".format(obj.content_object)

    def rating_value(self, obj):
        if obj.rating.type.name == STAR_RATING_TYPE:
            try:
                val = "".join(['<i class="fa fa-star"></i>' for _ in range(obj.rating.value)])
                return """<div style="min-width: {0}px;">{1}</div>""".format(obj.rating.value * 12, val)
            except TypeError:
                # None rating
                return "None"
        return obj.rating

    rating_value.allow_tags = True
    rating_value.short_description = "Rating"
    rating_value.admin_order_field = 'rating__value'
