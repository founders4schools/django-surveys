.. :changelog:

History
-------

Unreleased
++++++++++

0.4.0 (2017-03-10)
++++++++++++++++++

* [FEATURE] Template tags to send rating related emails
* Run tests against Django 1.11 and master
* [DOC] Added pull request template with basic checklist

0.3.1 (2017-01-04)
++++++++++++++++++

* [BUG] Fix migration for replaceable foreign key `Review.user`

0.3.0 (2016-12-23)
++++++++++++++++++

* [IMPROVEMENT] Added `on_delete=models.CASCADE` to all ForeignKeys,
  it'll become required in Django 2.0.
* [FEATURE] Added `created` and `updated` fields to all models using
  the `TimeStampedModel` from `Django model utils`_. generated 3
  migrations to preserve the existing `timestamp` that was present on
  the `Review` model.
* [DOC] Corrected links in Changelog

.. _Django model utils: https://django-model-utils.readthedocs.io/en/latest/models.html#timestampedmodel

0.2.0 (2016-12-23)
++++++++++++++++++

* `#5`_ [FEATURE] Ability to customise the reviewer model
* [IMPROVEMENT] Namespaced the app settings a la DRF

.. _#5: https://github.com/founders4schools/django-surveys/issues/5

0.1.1 (2016-12-23)
++++++++++++++++++

* `#6`_ [BUG] Fix error message when rating is out of bounds

.. _#6: https://github.com/founders4schools/django-surveys/issues/6

0.1.0 (2016-12-22)
++++++++++++++++++

* First release on PyPI.
