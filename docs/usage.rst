=====
Usage
=====

The app comes with a set of views for Django REST views and serializers.


Settings
========

All the possible customisations are namespaced under a main Django setting.
Each setting is a dictionary key.

The implementation is highly inspired by `Django REST Framework`_.

.. versionadded:: 0.2.0
    Namespaced all the settings under a single one

Example:

.. code-block:: python

    DJANGO_SURVEYS = {
        'FONT_AWESOME_CSS': None,
        'USER_HASH_FIELD': 'uuid',
    }

USER_HASH_FIELD
---------------

The field of the `User` model to use for the quick rating, default to `username`.


FONT_AWESOME_CSS
----------------

CSS file to use in the admin to render stars. Default to CDN served Font Awesome.

REVIEWER_MODEL
--------------

Similar to Django's `auth.User` model, you can override the model would be
used as user profile will be marked as the reviewer. this is a string to be
passed as argument of of `ForeignKey` field. Default to `settings.AUTH_USER_MODEL`.

STAR_LOGO_HTML
--------------

:todo: Add this setting to customise the HTML to render a star.

RATED_OBJECT_HASH_FIELD
-----------------------

:todo: Add this setting to customise which field is used to find the object being rated
       in the quick rating view.


.. _`Django REST Framework`: http://www.django-rest-framework.org/api-guide/settings/
