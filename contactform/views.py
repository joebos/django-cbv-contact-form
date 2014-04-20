"""Implements contact form view"""

import django.dispatch

contact_form_valid = django.dispatch.Signal(
    providing_args=['event', 'sender_ip', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

contact_form_invalid = django.dispatch.Signal(
    providing_args=['event', 'sender_ip', 'sender_name', 'sender_email']
)

from django.views.generic import CreateView

from braces.views import FormMessagesMixin

from contactform.conf import settings
from contactform.forms import ContactForm, ContactFormCaptcha


class ContactFormView(FormMessagesMixin, CreateView):
    """Contact form view"""

    template_name = 'contactform/form.html'
    success_url = settings.CONTACT_FORM_SUCCESS_URL

    form_valid_message = settings.CONTACT_FORM_VALID_MESSAGE
    form_invalid_message = settings.CONTACT_FORM_INVALID_MESSAGE

    valid_event = 'CONTACT_FORM_VALID_MESSAGE'
    invalid_event = 'CONTACT_FORM_INVALID_MESSAGE'

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
        return initial

    def form_valid(self, form):
        """This is what's called when the form is valid."""
        instance = form.save(commit=False)
        if hasattr(self.request, 'user'):
            instance.user = self.request.user
        instance.ip = self.request.META['REMOTE_ADDR']
        instance.save()
        if settings.CONTACT_FORM_USE_SIGNALS:
            contact_form_valid.send(
                sender=self,
                event=self.valid_event,
                ip=instance.ip,
                sender_name=instance.sender_name,
                sender_email=instance.sender_email,
                email=instance.subject.department.email,
                subject=instance.subject.title,
                message=instance.message
            )

        return super(ContactFormView, self).form_valid(form)

    def form_invalid(self, form):
        """This is what's called when the form is invalid."""
        ip = self.request.META['REMOTE_ADDR']
        if settings.CONTACT_FORM_USE_SIGNALS:
            contact_form_invalid.send(
                sender=self,
                event=self.invalid_event,
                ip=ip,
                sender_name=form['sender_name'],
                sender_email=form['sender_email']
            )

        return super(ContactFormView, self).form_invalid(form)