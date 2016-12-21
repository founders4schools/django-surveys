# -*- coding: utf-8
from django.apps import AppConfig


class SurveysConfig(AppConfig):
    name = 'surveys'

    def ready(self):
        from . import signals  # noqa
