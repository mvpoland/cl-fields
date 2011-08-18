cl-fields
=========
This contains some extra Django fields and field filters that we use at
`CityLive <http://citylive.be>`_ and `Mobile Vikings
<https://mobilevikings.com>`_.

Fields
------
JSONField
~~~~~~~~~
A TextField that serializes to JSON objects.

The initial version is based on `David Cramers blog post
<http://justcramer.com/2009/04/14/cleaning-up-with-json-and-sql/>`_.

Filters
-------
IsNullFilter
~~~~~~~~~~~~
Add a filter to the admin to only select whether a value is ``NULL`` or not.

Usage::

    list_filter = (
        ('parsed_on', IsNullFilter),
    )

**WARNING** Only works on Django 1.4
