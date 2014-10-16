# coding: utf-8

'''
Created on Apr 18, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from eventex.subscriptions.models import Subscription
from django.db import IntegrityError
from datetime import datetime

class SubscriptionTest(TestCase):
    
    def setUp(self):
        self.obj = Subscription(
            name='Rafael Cassau',
            cpf='12345678901',
            email='rafa_cassau@msn.com',
            phone='16-11111111'
        )
        
    def test_create(self):
        'Subscription must have name, cpf, email, phone.'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
    
    def test_has_created_at(self):
        'Subscription must have automatic created_at.'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_unicode(self):
        self.assertEqual(u'Rafael Cassau', unicode(self.obj))
        
    def test_paid_default_value_is_false(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)
    
class SubscriptionUniqueTest(TestCase):
    
    def setUp(self):
        'Create a first entry to force the collision.'
        Subscription.objects.create(
            name='Rafael Cassau',
            cpf='12345678901',
            email='rafa_cassau@msn.com',
            phone='16-11111111'
        )
        
    def test_cpf_unique(self):
        
        s = Subscription(
            name='Rafael Cassau',
            cpf='12345678901',
            email='outro@email.com',
            phone='16-11111111'
        )
        self.assertRaises(IntegrityError, s.save)
    
    def test_email_can_repeat(self):
        'Email is not unique anymore'
        s = Subscription.objects.create(
            name='Rafael Cassau',
            cpf='00000000001',
            email='rafa_cassau@msn.com',
            phone='16-11111111'
        )
        self.assertEqual(2, s.pk)
        