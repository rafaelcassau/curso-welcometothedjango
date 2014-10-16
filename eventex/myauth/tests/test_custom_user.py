# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.test.utils import override_settings
from django.test.testcases import TestCase
from django.contrib.auth import get_user_model

@override_settings(AUTH_USER_MODEL='myauth.User')
class FunctionalCustomUserTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        u = UserModel(cpf='12345678901')
        u.set_password('abracadabra')
        u.save()

    def test_login_with_cpf(self):
        self.assertTrue(self.client.login(cpf='12345678901', password='abracadabra'))