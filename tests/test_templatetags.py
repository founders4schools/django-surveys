import logging
from unittest import TestCase

from django.template import Context
from django.template import Template

logger = logging.getLogger(__name__)


def render_template(template_str, context_dict):
    body_template = Template(template_str)
    template_context = Context(context_dict)
    return body_template.render(template_context)


class TestTags(TestCase):
    def test_text_ok(self):
        """Should render links as text"""
        rendered = render_template(
            "{% load surveys_tags %}{% five_stars_text obj.rate_url %}",
            {'obj': {'rate_url': 'http://www.test.com/rate/wrqwi42y9t043gh0v/'}}
        )
        self.assertEqual(
            rendered,
            "\n"
            "Click here for a rating of 1\n"
            "http://www.test.com/rate/wrqwi42y9t043gh0v/?rating=1\n"
            "\n"
            "Click here for a rating of 2\n"
            "http://www.test.com/rate/wrqwi42y9t043gh0v/?rating=2\n"
            "\n"
            "Click here for a rating of 3\n"
            "http://www.test.com/rate/wrqwi42y9t043gh0v/?rating=3\n"
            "\n"
            "Click here for a rating of 4\n"
            "http://www.test.com/rate/wrqwi42y9t043gh0v/?rating=4\n"
            "\n"
            "Click here for a rating of 5\n"
            "http://www.test.com/rate/wrqwi42y9t043gh0v/?rating=5\n"
            "\n"
        )

    def test_text_cta(self):
        """Should render links as text with custom sentence"""
        rendered = render_template(
            "{% load surveys_tags %}{% five_stars_text obj.rate_url cta='Give a rating of' %}",
            {'obj': {'rate_url': 'http://www.test.com/rate/vjkdsg/'}}
        )
        self.assertEqual(
            rendered,
            "\n"
            "Give a rating of 1\n"
            "http://www.test.com/rate/vjkdsg/?rating=1\n"
            "\n"
            "Give a rating of 2\n"
            "http://www.test.com/rate/vjkdsg/?rating=2\n"
            "\n"
            "Give a rating of 3\n"
            "http://www.test.com/rate/vjkdsg/?rating=3\n"
            "\n"
            "Give a rating of 4\n"
            "http://www.test.com/rate/vjkdsg/?rating=4\n"
            "\n"
            "Give a rating of 5\n"
            "http://www.test.com/rate/vjkdsg/?rating=5\n"
            "\n"
        )

    def test_html_ok(self):
        """Should render links as HTML"""
        rendered = render_template(
            "{% load surveys_tags %}{% spaceless %}{% five_stars_html obj.rate_url %}{% endspaceless %}",
            {'obj': {'rate_url': 'http://www.test.com/rate/jkdgjhgds/'}}
        )
        self.assertIn(
            '<a href="http://www.test.com/rate/jkdgjhgds/?rating=1">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )
        self.assertIn(
            '<a href="http://www.test.com/rate/jkdgjhgds/?rating=2">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )
        self.assertIn(
            '<a href="http://www.test.com/rate/jkdgjhgds/?rating=3">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )
        self.assertIn(
            '<a href="http://www.test.com/rate/jkdgjhgds/?rating=4">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )
        self.assertIn(
            '<a href="http://www.test.com/rate/jkdgjhgds/?rating=5">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )

    def test_html_empty(self):
        """Should render links as HTML with empty URL if wrongly used"""
        rendered = render_template(
            "{% load surveys_tags %}{% spaceless %}{% five_stars_html obj.rate_url %}{% endspaceless %}",
            {'obj': None}
        )
        self.assertIn(
            '<a href="?rating=1">'
            '<img src="/static/surveys/img/rating_star-o.png"/>'
            '</a>', rendered
        )
