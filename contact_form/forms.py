"""Implements contact form forms"""

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings

try:
    import bleach
except ImportError:
    raise 'django-cbv-contact-form application required bleach package'

try:
    from captcha.fields import CaptchaField
except ImportError:
    raise 'django-cbv-contact-form application required django-simple-captcha package'

try:
    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Layout, Fieldset, Button, ButtonHolder, Submit
except ImportError:
    raise 'django-cbv-contact-form application required django-crispy-forms package'

from contact_form.conf import settings
from contact_form.models import Message, Subject


class ContactForm(forms.ModelForm):
    """ContactForm form"""

    if hasattr(django_settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        queryset = Subject.objects.filter(site__id=django_settings.SITE_ID)
    else:
        queryset = Subject.objects.all()
    subject = forms.ModelChoiceField(queryset=queryset,
                                     widget=forms.Select(),
                                     label=_('Message subject'),
                                     empty_label=_('Please select subject'),
                                     error_messages={'required': _('Please select subject')})
    sender_name = forms.CharField(label=_('Your name'),
                                  widget=forms.TextInput(
                                      attrs={'maxlength': settings.CONTACT_FORM_SENDER_NAME_MAX_LENGTH}
                                  ),
                                  error_messages={'required': _('Please enter your name')})
    # maxlength is 254 characters for compliant with RFCs 3696 and 5321
    sender_email = forms.EmailField(label=_('Your e-mail'),
                                    widget=forms.TextInput(attrs={'maxlength': 254}),
                                    error_messages={'required': _('Please enter your email.')})
    message = forms.CharField(label=_('Your message'),
                              widget=forms.Textarea(attrs={'maxlength': settings.CONTACT_FORM_MESSAGE_MAX_LENGTH}),
                              min_length=settings.CONTACT_FORM_MESSAGE_MIN_LENGTH,
                              help_text=_('Your message ({0} characters minimum)').format(
                                  settings.CONTACT_FORM_MESSAGE_MIN_LENGTH
                              ),
                              error_messages={'required': _('Please enter your message'),
                                              'min_length': _('Use at least {0} characters').format(
                                                  settings.CONTACT_FORM_MESSAGE_MIN_LENGTH
                                              )})

    def __init__(self, *args, **kwargs):
        """Form initialization method

        :param args: form args
        :param kwargs: form keyword args
        """
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Contact form'),
                'subject',
                'sender_name',
                'sender_email',
                'message',
            ),
            ButtonHolder(
                Button('cancel', _('Cancel'), css_class='secondaryAction'),
                Submit('submit', _('Submit'), css_class='primaryAction'),
            )
        )
        self.helper.add_layout(layout)
        self.helper.form_id = 'contact_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.form_style = 'inline'

        super(ContactForm, self).__init__(*args, **kwargs)

    def clean_sender_name(self):
        data = self.cleaned_data['sender_name']
        if settings.CONTACT_FORM_FILTER_SENDER_NAME:
            if len(data) != len(bleach.clean(data, tags=[], strip=True)):
                raise forms.ValidationError(_('Not allowed characters in your name'))
        return data

    def clean_message(self):
        data = self.cleaned_data['message']
        if settings.CONTACT_FORM_FILTER_MESSAGE:
            if len(data) != len(bleach.clean(data, tags=settings.CONTACT_FORM_ALLOWED_MESSAGE_TAGS, strip=True)):
                raise forms.ValidationError(_('Not allowed characters in your message'))
        return data

    class Meta:
        model = Message
        fields = (
            'subject',
            'sender_name',
            'sender_email',
            'message',
        )


class ContactFormCaptcha(ContactForm):
    """ContactForm form with captcha"""

    captcha = CaptchaField(label=_('Protection Code'),
                           error_messages={'required': _('Please enter protection code'),
                                           'invalid': _('Invalid protection code')})

    def __init__(self, *args, **kwargs):
        """Form initialization method

        :param args: form args
        :param kwargs: form keyword args
        """
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Contact form'),
                'subject',
                'sender_name',
                'sender_email',
                'message',
                'captcha',
            ),
            ButtonHolder(
                Button('cancel', _('Cancel'), css_class='secondaryAction'),
                Submit('submit', _('Submit'), css_class='primaryAction'),
            )
        )
        self.helper.add_layout(layout)
        self.helper.form_id = 'contact_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.form_style = 'inline'

        super(ContactForm, self).__init__(*args, **kwargs)
