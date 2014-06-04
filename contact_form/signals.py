import django.dispatch

contact_form_valid = django.dispatch.Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email', 'email', 'subject', 'message']
)

contact_form_invalid = django.dispatch.Signal(
    providing_args=['event', 'ip', 'site', 'sender_name', 'sender_email']
)