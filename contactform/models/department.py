"""Implements contact form Department model"""

from django.db import models
from django.utils.translation import ugettext as _

from contactform.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=settings.CONTACT_FORM_MAX_DEPARTMENT_NAME_LENGTH)
    email = models.EmailField()
    phone = models.CharField(max_length=settings.CONTACT_FORM_MAX_DEPARTMENT_PHONE_LENGTH, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def get_absolute_url(self):
        return u'/department/{0:>s}'.format(self.id)

    class Meta:
        app_label = 'contactform'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

