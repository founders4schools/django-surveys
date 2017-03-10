# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django import template

register = template.Library()


@register.inclusion_tag('surveys/survey-star-o.svg')
def star_svg(width=50, color=None):
    return {
        'width': width,
        'color': color,
    }


@register.inclusion_tag('surveys/5-stars.html')
def five_stars_html(object_rate_url):
    """Helper to include rating links in a HTML email"""
    return {
        'object_rate_url': object_rate_url,
    }


@register.inclusion_tag('surveys/5-stars.txt')
def five_stars_text(object_rate_url, cta="Click here for a rating of"):
    """Helper to include rating links in a text email"""
    return {
        'cta': cta,
        'object_rate_url': object_rate_url,
    }
