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
