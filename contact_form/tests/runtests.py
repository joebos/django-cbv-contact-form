#!/usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
test_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, test_dir)

import django
if django.VERSION >= (1, 7):
    django.setup()

if django.VERSION < (1, 6):
    from django.test.simple import DjangoTestSuiteRunner as TestRunner
else:
    from django.test.runner import DiscoverRunner as TestRunner

from django.conf import settings


def runtests():
    test_runner = TestRunner(settings, failfast=False, verbosity=1, interactive=True)
    failures = test_runner.run_tests(['contact_form.tests.TestContactForm'])
    return bool(failures)

if __name__ == '__main__':
    sys.exit(runtests())
