"""Implements contact form admin interface"""

from __future__ import unicode_literals

from django.contrib import admin
from django.core import urlresolvers
from django.conf import settings as django_settings
from django.utils.translation import ugettext as _

from contact_form.models import *
from contact_form.conf import settings

try:
    from modeltranslation.admin import TranslationAdmin

    class SubjectBaseAdmin(TranslationAdmin):
        pass
except ImportError:
    class SubjectBaseAdmin(admin.ModelAdmin):
        pass


class SubjectAdmin(SubjectBaseAdmin):
    if hasattr(django_settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        list_display = ('title', 'department_url', 'site')
    else:
        list_display = ('title', 'department_url')
        exclude = ('site', )

    def department_url(self, obj):
        change_url = urlresolvers.reverse('admin:contact_form_department_change', args=(obj.department.id,))
        return '<a href="{0:>s}">{1:>s}</a>'.format(change_url, obj.department.name)
    department_url.allow_tags = True
    department_url.short_description = _('Department')

admin.site.register(Subject, SubjectAdmin)
