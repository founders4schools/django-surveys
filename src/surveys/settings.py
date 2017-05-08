# -*- coding: utf-8
"""
App settings inspired by Django REST Framework's

Settings are namespaced under 'DJANGO_SURVEYS' in your
project's settings.py::

    DJANGO_SURVEYS = {
        'FONT_AWESOME_CSS': None,
        'USER_HASH_FIELD': 'uuid',
        'REVIEWER_MODEL': 'users.Reviewer',
    }
"""
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.core.signals import setting_changed

DEFAULTS = {
    'FONT_AWESOME_CSS': '//maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css',
    'USER_HASH_FIELD': 'username',
    'REVIEWER_MODEL': settings.AUTH_USER_MODEL,
}

SETTING_NAMESPACE = 'DJANGO_SURVEYS'


class AppSettings(object):
    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, SETTING_NAMESPACE, {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


surveys_settings = AppSettings(None, DEFAULTS)


def reload_settings(*args, **kwargs):  # pylint:disable=unused-argument
    global surveys_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == SETTING_NAMESPACE:
        surveys_settings = AppSettings(value, DEFAULTS)


setting_changed.connect(reload_settings)
