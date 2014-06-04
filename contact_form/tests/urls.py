from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # captcha support urls
    url(r'^captcha/', include('captcha.urls')),

    # contact_form
    (r'^contact_form/', include('contact_form.urls')),
)
