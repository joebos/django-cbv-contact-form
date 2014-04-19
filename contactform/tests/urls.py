from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # captcha support urls
    url(r'^captcha/', include('captcha.urls')),

    # contactform
    (r'^contactform/', include('contactform.urls')),
)

