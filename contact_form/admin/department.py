"""Implements contact form admin interface"""

from django.contrib import admin

from contact_form.models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(Department, DepartmentAdmin)
