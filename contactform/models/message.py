"""Implements contact form Message model"""

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from contactform.models.subject import Subject
from contactform.conf import settings


class Message(models.Model):
    sender_name = models.CharField(max_length=settings.CONTACT_FORM_MAX_SENDER_NAME_LENGTH, verbose_name=_('Sender name'))
    sender_email = models.EmailField(verbose_name=_('Sender email'))
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'), max_length=settings.CONTACT_FORM_MAX_MESSAGE_LENGTH)
    ip = models.IPAddressField(_('IP'), null=True, blank=True)
    date_created = models.DateTimeField(_('Created'), default=timezone.now)

    def __unicode__(self):
        return u'{0:>n}'.format(self.pk)

    class Meta:
        app_label = 'contactform'
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
