"""Implements contact form views"""

import django.dispatch

contact_form_message = django.dispatch.Signal(
    providing_args=['event', 'sender_ip', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from braces.views import FormMessagesMixin

from contactform.conf import settings
from contactform.forms import ContactForm, ContactFormCaptcha


class ContactFormView(FormMessagesMixin, CreateView):
    """Contact form view"""

    template_name = 'contactform/form.html'
    success_url = reverse_lazy('contactform')
    # TODO: replace to configurable strings
    form_valid_message = _(u'Your message is submitted.')
    form_invalid_message = _(u'Something went wrong, your message was not submitted!')

    success_event = 'CONTACT_FORM_NEW_MESSAGE'

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
                    sender_name = user[settings.CONTACT_FORM_USERNAME_FIELD]
                if hasattr(user, settings.CONTACT_FORM_USER_EMAIL_FIELD):
                    sender_email = user[settings.CONTACT_FORM_USER_EMAIL_FIELD]
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
            contact_form_message.send(
                sender=self,
                event=self.success_event,
                ip=instance.ip,
                sender_name=instance.sender_name,
                sender_email=instance.sender_email,
                email=instance.subject.department.email,
                subject=instance.subject.title,
                message=instance.message
            )

        return super(ContactFormView, self).form_valid(form)