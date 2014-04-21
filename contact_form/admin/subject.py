"""Implements contact form admin interface"""

from django.contrib import admin
from django.core import urlresolvers
from django.utils.translation import ugettext as _

from contact_form.models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department_url')

    def department_url(self, obj):
        change_url = urlresolvers.reverse('admin:contact_form_department_change', args=(obj.department.id,))
        return u'<a href="{0:>s}">{1:>s}</a>'.format(change_url, obj.department.name)
    department_url.allow_tags = True
    department_url.short_description = _('Department')

admin.site.register(Subject, SubjectAdmin)
