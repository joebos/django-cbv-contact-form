
from django.conf import settings

CONTACT_FORM_USE_CAPTCHA = getattr(settings, 'CONTACT_FORM_USE_CAPTCHA', False)
CONTACT_FORM_USE_SIGNALS = getattr(settings, 'CONTACT_FORM_USE_SIGNALS', False)

CONTACT_FORM_USE_USERNAME = getattr(settings, 'CONTACT_FORM_USE_USERNAME', True)
CONTACT_FORM_USERNAME_FIELD = getattr(settings, 'CONTACT_FORM_USERNAME_FIELD', 'username')
CONTACT_FORM_USE_USER_EMAIL = getattr(settings, 'CONTACT_FORM_USE_USER_EMAIL', True)
CONTACT_FORM_USER_EMAIL_FIELD = getattr(settings, 'CONTACT_FORM_USER_EMAIL_FIELD', 'email')

CONTACT_FORM_MAX_SENDER_NAME_LENGTH = getattr(settings, 'CONTACT_FORM_MAX_SENDER_NAME_LENGTH', 80)
CONTACT_FORM_MAX_SUBJECT_LENGTH = getattr(settings, 'CONTACT_FORM_MAX_SUBJECT_LENGTH', 80)
CONTACT_FORM_MAX_MESSAGE_LENGTH = getattr(settings, 'CONTACT_FORM_MAX_SUBJECT_LENGTH', 4096)

CONTACT_FORM_MAX_DEPARTMENT_NAME_LENGTH = getattr(settings, 'CONTACT_FORM_MAX_DEPARTMENT_NAME_LENGTH', 80)
CONTACT_FORM_MAX_DEPARTMENT_PHONE_LENGTH = getattr(settings, 'CONTACT_FORM_MAX_DEPARTMENT_PHONE_LENGTH', 20)