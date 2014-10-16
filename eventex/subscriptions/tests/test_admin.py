# coding: utf-8

'''
Created on Apr 19, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkAsPaidTest(TestCase):
    
    def setUp(self):
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Rafael Cassau',
                                    cpf='11111111111',
                                    email='rafa_cassau@msn.com')
    
    def test_has_action(self):
        'Action is installed.'
        self.assertIn('mark_as_paid', self.model_admin.actions)
        
    def test_mark_all(self):
        'Mark all as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
    
    