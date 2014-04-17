django-cbv-contact-form
=======================

Class based view contact form with captcha support for Django 1.5+

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "contactform" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'contactform',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^contactform/', include('contactform.urls')),

3.  For create the contact form models run:

    `python manage.py syncdb`  for Django 1.5+

    `python manage.py migrate` for Django 1.7+

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to setup contact form settings (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/contactform/ to use contact form.
