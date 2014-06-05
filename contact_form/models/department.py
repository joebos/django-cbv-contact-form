"""Implements contact form Department model"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible

from contact_form.conf import settings


@python_2_unicode_compatible
class Department(models.Model):
    name = models.CharField(max_length=settings.CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH)
    # max_length overridden to 254 characters for compliant with RFCs 3696 and 5321
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=settings.CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH, blank=True)
    site = models.ForeignKey(Site, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/department/{0:>s}'.format(self.id)

    class Meta:
        app_label = 'contact_form'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
