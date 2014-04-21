
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client, RequestFactory

from contact_form.models import Message, Department, Subject


class ContactFormCase(TestCase):
    urls = 'contact_form.tests.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user_foo = User.objects.create(username='foo', password='bar', email='foo@test.com')
        self.department_foo = Department.objects.create(name='foo department', email='department@test.com')
        self.subject_foo = Subject.objects.create(title='test subject title', department=self.department_foo)
        self.message_foo = Message.objects.create(
            sender_name='foo',
            sender_email='foo@test.com',
            subject=self.subject_foo,
            message='test message text',
            ip='127.0.0.1')

    def tearDown(self):
        self.user_foo.delete()
        self.message_foo.delete()
        self.subject_foo.delete()
        self.department_foo.delete()

