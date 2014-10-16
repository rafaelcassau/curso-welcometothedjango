# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from eventex.myauth.backends import EmailBackend
from django.test.utils import override_settings
from unittest import skip


@skip
class EmailBackendTest(TestCase):
    
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='henrique',
            email='henrique@bastos.net',
            password='abracadabra'
        )
        self.backend = EmailBackend()
        
    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='henrique@bastos.net', password='abracadabra')
        self.assertIsNotNone(user)
    
    def test_wrong_password(self):
        user = self.backend.authenticate(email='henrique@bastos.net', password='wrong')
        self.assertIsNone(user)
    
    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@email.com', password='abracadabra')
        self.assertIsNone(user)
    
    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))


@skip
class MultipleEmailsTest(TestCase):
    
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
        email='henrique@bastos.net', password='abracadabra')
        UserModel.objects.create_user(username='user2',
        email='henrique@bastos.net', password='abracadabra')
        self.backend = EmailBackend()
        
    def test_multiple_emails(self):
        user = self.backend.authenticate(email='henrique@bastos.net',
        password='abracadabra')
        self.assertIsNone(user)


@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
    
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='henrique',
            email='henrique@bastos.net',
            password='abracadabra'
        )
        
    def test_login_with_email(self):
        result = self.client.login(email='henrique@bastos.net', password='abracadabra')
        self.assertTrue(result)
        
    def test_login_with_username(self):
        result = self.client.login(username='henrique@bastos.net', password='abracadabra')
        self.assertTrue(result)
