Django class based contact form
===============================

``django-cbv-contact-form`` is a class based view contact form with captcha support for Django 1.5+

Requirements
------------

::

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

    $ pip install -e git+http://github.com/dlancer/django-cbv-contact-form.git#egg=contact_form-dev

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
        'contact_form',
    )

Include the contact form URLconf in your project urls.py like this::

    urlpatterns = patterns(
    '',
        ...
        url(r'^captcha/', include('captcha.urls')),
        url(r'^contact_form/', include('contact_form.urls')),
    )

Run ``python manage.py syncdb``.  This creates the appropriate tables in your database
that are necessary for operation.

Database migration
------------------

If you use Django 1.5+ you can use database migration by add South application to your django settings.
Django 1.7+ has native database migration support.


Customizing contact form
------------------------

You have a lot of options available to you to customize ``django-cbv-contact-form``.
These options should be defined in your ``settings.py`` file.

**Contact form logic customization**

* ``CONTACT_FORM_USE_CAPTCHA``: force use captcha for anonymous users

* ``CONTACT_FORM_USE_SIGNALS``: send signals after form submitting

* ``CONTACT_FORM_SUCCESS_URL``: url for redirection after successful form submission

**Contact form submission message customization**

* ``CONTACT_FORM_VALID_MESSAGE``: success message for valid form submission

* ``CONTACT_FORM_INVALID_MESSAGE``: error message for invalid form submission

**User model related customization**

* ``CONTACT_FORM_USE_USERNAME``: fill username form field for authenticated user

* ``CONTACT_FORM_USERNAME_FIELD``: username field name in User model

* ``CONTACT_FORM_USE_USER_EMAIL``: fill email form field for authenticated user

* ``CONTACT_FORM_USER_EMAIL_FIELD``: email field name in User model

**Contact form models fields customization**

* ``CONTACT_FORM_SENDER_NAME_MAX_LENGTH``: sender name maximum length

* ``CONTACT_FORM_SUBJECT_MAX_LENGTH``: message subject maximum length

* ``CONTACT_FORM_MESSAGE_MAX_LENGTH``: message text maximum length

* ``CONTACT_FORM_MESSAGE_MIN_LENGTH``: message text minimum length

* ``CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH``: department name maximum length

* ``CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH``: department phone maximum length

Usage
=====

Start the development server and visit http://127.0.0.1:8000/admin/ to setup contact
form settings (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/contact_form/ to use contact form.


You may find detailed documentation is in the "docs" directory.