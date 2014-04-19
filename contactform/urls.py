"""Django urls for contact form."""

from django.conf.urls import patterns, url

from contactform.views import ContactFormView

urlpatterns = patterns('', url(r'^$', ContactFormView.as_view(), name='contactform'), )

