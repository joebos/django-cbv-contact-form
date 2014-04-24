"""Implements contact form Subject model"""

from django.db import models
from django.utils.translation import ugettext as _

from contact_form.conf import settings
from contact_form.models.department import Department


class Subject(models.Model):
    title = models.CharField(max_length=settings.CONTACT_FORM_SUBJECT_MAX_LENGTH)
    department = models.ForeignKey(Department)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)

    class Meta:
        app_label = 'contact_form'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

