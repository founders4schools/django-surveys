============
Installation
============

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

Run migrations::

    python manage.py migrate


