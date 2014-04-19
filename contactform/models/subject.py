"""Implements contact form Subject model"""

from django.db import models
from django.utils.translation import ugettext as _

from contactform.conf import settings
from contactform.models.department import Department


class Subject(models.Model):
    title = models.CharField(max_length=settings.CONTACT_FORM_MAX_SUBJECT_LENGTH)
    department = models.ForeignKey(Department)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)

    class Meta:
        app_label = 'contactform'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

