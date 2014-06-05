from __future__ import unicode_literals
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

CONTACT_FORM_USE_CAPTCHA = getattr(settings, 'CONTACT_FORM_USE_CAPTCHA', False)
CONTACT_FORM_USE_SIGNALS = getattr(settings, 'CONTACT_FORM_USE_SIGNALS', False)
CONTACT_FORM_SUCCESS_URL = getattr(settings, 'CONTACT_FORM_SUCCESS_URL', reverse_lazy('contact_form'))
CONTACT_FORM_USE_SITES = getattr(settings, 'CONTACT_FORM_USE_SITES', True)
CONTACT_FORM_FILTER_SENDER_NAME = getattr(settings, 'CONTACT_FORM_FILTER_SENDER_NAME', True)
CONTACT_FORM_FILTER_MESSAGE = getattr(settings, 'CONTACT_FORM_FILTER_MESSAGE', True)
CONTACT_FORM_ALLOWED_MESSAGE_TAGS = getattr(settings, 'CONTACT_FORM_ALLOWED_MESSAGE_TAGS', [])
CONTACT_FORM_STRIP_MESSAGE = getattr(settings, 'CONTACT_FORM_STRIP_MESSAGE', False)

CONTACT_FORM_VALID_MESSAGE = getattr(
    settings,
    'CONTACT_FORM_VALID_MESSAGE',
    _('Your message is submitted.')
)

CONTACT_FORM_INVALID_MESSAGE = getattr(
    settings,
    'CONTACT_FORM_INVALID_MESSAGE',
    _('Something went wrong, your message was not submitted!')
)

CONTACT_FORM_USE_USERNAME = getattr(settings, 'CONTACT_FORM_USE_USERNAME', True)
CONTACT_FORM_USERNAME_FIELD = getattr(settings, 'CONTACT_FORM_USERNAME_FIELD', 'username')
CONTACT_FORM_USE_USER_EMAIL = getattr(settings, 'CONTACT_FORM_USE_USER_EMAIL', True)
CONTACT_FORM_USER_EMAIL_FIELD = getattr(settings, 'CONTACT_FORM_USER_EMAIL_FIELD', 'email')

CONTACT_FORM_SENDER_NAME_MAX_LENGTH = getattr(settings, 'CONTACT_FORM_SENDER_NAME_MAX_LENGTH', 80)
CONTACT_FORM_SUBJECT_MAX_LENGTH = getattr(settings, 'CONTACT_FORM_SUBJECT_MAX_LENGTH', 80)
CONTACT_FORM_MESSAGE_MAX_LENGTH = getattr(settings, 'CONTACT_FORM_MESSAGE_MAX_LENGTH', 4096)
CONTACT_FORM_MESSAGE_MIN_LENGTH = getattr(settings, 'CONTACT_FORM_MESSAGE_MIN_LENGTH', 15)

CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH = getattr(settings, 'CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH', 80)
CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH = getattr(settings, 'CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH', 20)
