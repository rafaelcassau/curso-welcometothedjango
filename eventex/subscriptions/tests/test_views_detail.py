# coding: utf-8

'''
Created on Apr 19, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse

class DetailTest(TestCase):
    
    def setUp(self):
        s = Subscription.objects.create(
                name='Rafael Cassau',
                cpf='12345678901',
                email='rafa_cassau@msn.com',
                phone='21-111111111'
            )
        self.resp = self.client.get(reverse('subscriptions:detail', args=[s.pk]))
    
    def test_get(self):
        'GET /inscricao/1/ should return status 200.'
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        'Uses template.'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')
    
    def test_context(self):
        'Context must have a subscription instance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)
    
    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, 'Rafael Cassau')
    
class DetailNotFound(TestCase):
    
    def test_not_found(self):
        response = self.client.get(reverse('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
        
        