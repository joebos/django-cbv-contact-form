Django class based contact form
===============================

``django-cbv-contact-form`` is a class based view contact form with captcha support for Django 1.5+

Requirements
------------

    django >= 1.5
    django-simple-captcha >= 0.4.2
    django-braces >= 1.4.0
    django-crispy-forms >= 1.4.0

Installation
============

Download and install ``django-cbv-contact-form`` using **one** of the following methods:

PIP
---

You can install the latest stable package running this command::

    $ pip install django-cbv-contact-form

Also you can install the development version running this command::

    $ pip install -e git+http://github.com/dlancer/django-cbv-contact-form.git#egg=contactform-dev

Setuptools
----------

You can install the latest stable package running::

    $ easy_install django-cbv-contact-form

Configuration
=============

You must add these apps to your list of ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'captcha',
        'braces',
        'crispy_forms',
        'contactform',
    )

Include the contact form URLconf in your project urls.py like this::

    urlpatterns = patterns(
    '',
        ...
        url(r'^captcha/', include('captcha.urls')),
        url(r'^contactform/', include('contactform.urls')),
    )

Run ``python manage.py syncdb``.  This creates the appropriate tables in your database
that are necessary for operation.

Customizing contact form
------------------------

You have a lot of options available to you to customize ``django-cbv-contact-form``.
These options should be defined in your ``settings.py`` file.

**Contact form logic customization**

- ``CONTACT_FORM_USE_CAPTCHA``: force use captcha for anonymous users

- ``CONTACT_FORM_USE_SIGNALS``: send signal after success form submitting

**User model related customization**

- ``CONTACT_FORM_USE_USERNAME``: fill username form field for authenticated user

- ``CONTACT_FORM_USERNAME_FIELD``: username field name in User model

- ``CONTACT_FORM_USE_USER_EMAIL``: fill email form field for authenticated user

- ``CONTACT_FORM_USER_EMAIL_FIELD``: email field name in User model

**Contact form models fields customization**

- ``CONTACT_FORM_MAX_SENDER_NAME_LENGTH``: sender name max length

- ``CONTACT_FORM_MAX_SUBJECT_LENGTH``: message subject max length
- ``CONTACT_FORM_MAX_MESSAGE_LENGTH``: message text max length

- ``CONTACT_FORM_MAX_DEPARTMENT_NAME_LENGTH``: department name max length
- ``CONTACT_FORM_MAX_DEPARTMENT_PHONE_LENGTH``: department phone max length

Usage
=====

Start the development server and visit http://127.0.0.1:8000/admin/ to setup contact
form settings (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/contactform/ to use contact form.


Detailed documentation is in the "docs" directory.