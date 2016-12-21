# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings

SURVEYS_FONT_AWESOME_CSS = getattr(settings, 'SURVEYS_FONT_AWESOME_CSS',
                                   '//maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css')

USER_HASH_FIELD = getattr(settings, 'SURVEYS_USER_HASH_FIELD', 'username')
