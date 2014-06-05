"""Implements contact form admin interface"""

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf import settings as django_settings

from contact_form.models import *
from contact_form.conf import settings


class MessageAdmin(admin.ModelAdmin):
    if hasattr(django_settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        list_display = ('subject', 'sender', 'ip', 'site', 'date_created_short')
        list_filter = ('date_created', 'subject')
        search_fields = ('sender_name', 'ip', 'site', 'date_created')
    else:
        list_display = ('subject', 'sender', 'ip', 'date_created_short')
        list_filter = ('date_created', 'subject')
        search_fields = ('sender_name', 'ip', 'date_created')
        exclude = ('site', )

    def sender(self, obj):
        return '<a href="mailto:{0:>s}">{1:>s}</a>'.format(obj.sender_email, obj.sender_name)
    sender.allow_tags = True
    sender.short_description = _('Sender')

    def date_created_short(self, obj):
        return obj.date_created.strftime('%Y/%m/%d %H:%M:%S')
    date_created_short.short_description = _('Created')
    date_created_short.admin_order_field = 'date_created'

admin.site.register(Message, MessageAdmin)
