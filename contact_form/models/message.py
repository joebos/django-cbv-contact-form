"""Implements contact form Message model"""

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible

from contact_form.models.subject import Subject
from contact_form.conf import settings


@python_2_unicode_compatible
class Message(models.Model):
    sender_name = models.CharField(
        max_length=settings.CONTACT_FORM_SENDER_NAME_MAX_LENGTH,
        verbose_name=_('Sender name')
    )
    # max_length overridden to 254 characters for compliant with RFCs 3696 and 5321
    sender_email = models.EmailField(verbose_name=_('Sender email'), max_length=254)
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'), max_length=settings.CONTACT_FORM_MESSAGE_MAX_LENGTH)
    ip = models.IPAddressField(_('IP'), null=True, blank=True)
    date_created = models.DateTimeField(_('Created'), default=timezone.now)
    site = models.ForeignKey(Site, null=True, blank=True)

    def __str__(self):
        return 'message {0:>n}'.format(self.pk)

    class Meta:
        app_label = 'contact_form'
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
