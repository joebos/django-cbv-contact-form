"""Implements contact form admin interface"""

from __future__ import unicode_literals

from django.contrib import admin
from django.conf import settings as django_settings

from contact_form.models import *
from contact_form.conf import settings


class DepartmentAdmin(admin.ModelAdmin):
    if hasattr(django_settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        list_display = ('name', 'email', 'phone', 'site')
    else:
        list_display = ('name', 'email', 'phone')
        exclude = ('site', )

admin.site.register(Department, DepartmentAdmin)
