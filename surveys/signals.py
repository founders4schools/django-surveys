# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.dispatch import Signal

post_rating = Signal(providing_args=['instance', 'value', 'is_negative'])
