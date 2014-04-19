#!/usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, parent)

from django import VERSION

if VERSION < (1, 6):
    from django.test.simple import DjangoTestSuiteRunner as TestRunner
else:
    from django.test.runner import DiscoverRunner as TestRunner


def runtests():
    return TestRunner(failfast=False).run_tests(
        ['contactform.tests.TestContactForm'], verbosity=1, interactive=True
    )


if __name__ == '__main__':
    if runtests():
        sys.exit(1)