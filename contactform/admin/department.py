"""Implements contact form admin interface"""

from django.contrib import admin

from contactform.models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(Department, DepartmentAdmin)
