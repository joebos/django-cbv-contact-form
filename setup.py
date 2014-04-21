import os
from setuptools import setup, find_packages
from contact_form import get_version as get_package_version

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cbv-contact-form',
    version=get_package_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'docutils>=0.3',
        'Django>=1.5',
        'django-simple-captcha>=0.4.2',
        'django-braces>=1.4.0',
        'django-crispy-forms>=1.4.0'
    ],
    license='MIT',
    description='Class based view contact form with captcha support for Django 1.5+',
    long_description=README,
    url='https://github.com/dlancer/django-cbv-contact-form',
    bugtrack_url='https://github.com/dlancer/django-cbv-contact-form/issues',
    author='dlancer',
    author_email='dmdpost@gmail.com',
    maintainer='dlancer',
    maintainer_email='dmdpost@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 2 - Pre-Alpha',
    ],
)