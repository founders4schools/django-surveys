=====
Usage
=====

The app comes with a set of views for Django REST views and serializers.


Settings
========


SURVEYS_USER_HASH_FIELD
-----------------------

The field of the `User` model to use for the quick rating, default to `username`.


SURVEYS_FONT_AWESOME_CSS
------------------------

CSS file to use in the admin to render stars. Default to CDN served Font Awesome.

SURVEYS_STAR_LOGO_HTML
----------------------

:todo: Add this setting to customise the HTML to render a star.

SURVEYS_RATED_OBJECT_HASH_FIELD
-------------------------------

:todo: Add this setting to customise which field is used to find the object being rated
       in the quick rating view.
