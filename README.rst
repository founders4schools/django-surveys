==============
Django Surveys
==============

.. image:: https://badge.fury.io/py/django-surveys.svg
    :target: https://badge.fury.io/py/django-surveys
    :alt: PyPI

.. image:: https://travis-ci.org/founders4schools/django-surveys.svg?branch=master
    :target: https://travis-ci.org/founders4schools/django-surveys
    :alt: Build

.. image:: https://readthedocs.org/projects/django-surveys/badge/?version=latest
    :target: http://django-surveys.readthedocs.io
    :alt: Docs

.. image:: https://landscape.io/github/founders4schools/django-surveys/master/landscape.svg?style=flat
    :target: https://landscape.io/github/founders4schools/django-surveys/master
    :alt: Code Health

A reusable Django app that lets users write feedback for any model

Documentation
-------------

The full documentation is at https://django-surveys.readthedocs.io.

Quickstart
----------

Install Django Surveys::

    pip install django-surveys

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'surveys.apps.SurveysConfig',
        ...
    )

Add Django Surveys's URL patterns:

.. code-block:: python

    from surveys import urls as surveys_urls


    urlpatterns = [
        ...
        url(r'^', include(surveys_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
