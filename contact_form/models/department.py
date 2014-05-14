"""Implements contact form Department model"""

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site

from contact_form.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=settings.CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH)
    # max_length overridden to 254 characters for compliant with RFCs 3696 and 5321
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=settings.CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH, blank=True)
    site = models.ForeignKey(Site, null=True, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def get_absolute_url(self):
        return u'/department/{0:>s}'.format(self.id)

    class Meta:
        app_label = 'contact_form'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

