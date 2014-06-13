"""Implements contact form view"""

from __future__ import unicode_literals

from django.views.generic import CreateView
from django.conf import settings as django_settings


try:
    import bleach
except ImportError:
    raise 'django-cbv-contact-form application required bleach package'

try:
    from braces.views import FormMessagesMixin
except ImportError:
    raise 'django-cbv-contact-form application required django-braces package'


from contact_form.conf import settings
from contact_form.forms import ContactForm, ContactFormCaptcha
from contact_form.signals import contact_form_valid, contact_form_invalid
from contact_form.helpers import get_user_ip


class ContactFormView(FormMessagesMixin, CreateView):
    """Contact form view"""

    template_name = 'contact_form/form.html'
    success_url = settings.CONTACT_FORM_SUCCESS_URL

    form_valid_message = settings.CONTACT_FORM_VALID_MESSAGE
    form_invalid_message = settings.CONTACT_FORM_INVALID_MESSAGE

    valid_event = 'CONTACT_FORM_VALID_MESSAGE'
    invalid_event = 'CONTACT_FORM_INVALID_MESSAGE'

    site = None

    def get_form_class(self):
        if hasattr(self.request, 'user'):
            is_authenticated = self.request.user.is_authenticated()
        else:
            is_authenticated = False
        if not is_authenticated and settings.CONTACT_FORM_USE_CAPTCHA:
            self.form_class = ContactFormCaptcha
        else:
            self.form_class = ContactForm
        return self.form_class

    def get_initial(self):
        sender_name = ''
        sender_email = ''
        if hasattr(self.request, 'user'):
            user = self.request.user
            if settings.CONTACT_FORM_USE_USERNAME and user.is_authenticated():
                if hasattr(user, settings.CONTACT_FORM_USERNAME_FIELD):
                    sender_name = getattr(user, settings.CONTACT_FORM_USERNAME_FIELD)
                if hasattr(user, settings.CONTACT_FORM_USER_EMAIL_FIELD):
                    sender_email = getattr(user, settings.CONTACT_FORM_USER_EMAIL_FIELD)
        initial = {'sender_name': sender_name, 'sender_email': sender_email}
        if hasattr(django_settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
            from django.contrib.sites.models import Site
            site = Site.objects.get(id=django_settings.SITE_ID)
            self.site = site
        return initial

    def form_valid(self, form):
        """This is what's called when the form is valid."""
        instance = form.save(commit=False)
        if hasattr(self.request, 'user'):
            instance.user = self.request.user
        if settings.CONTACT_FORM_FILTER_MESSAGE:
            instance.message = bleach.clean(
                instance.message,
                tags=settings.CONTACT_FORM_ALLOWED_MESSAGE_TAGS,
                strip=settings.CONTACT_FORM_STRIP_MESSAGE
            )
        instance.ip = get_user_ip(self.request)
        instance.site = self.site
        instance.save()
        if settings.CONTACT_FORM_USE_SIGNALS:
            contact_form_valid.send(
                sender=self,
                event=self.valid_event,
                ip=instance.ip,
                site=self.site,
                sender_name=instance.sender_name,
                sender_email=instance.sender_email,
                email=instance.subject.department.email,
                subject=instance.subject.title,
                message=instance.message
            )
        return super(ContactFormView, self).form_valid(form)

    def form_invalid(self, form):
        """This is what's called when the form is invalid."""
        ip = get_user_ip(self.request)
        if settings.CONTACT_FORM_USE_SIGNALS:
            contact_form_invalid.send(
                sender=self,
                event=self.invalid_event,
                ip=ip,
                site=self.site,
                sender_name=form['sender_name'],
                sender_email=form['sender_email']
            )

        return super(ContactFormView, self).form_invalid(form)


