# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from eventex.core.models import Talk
from django.core.urlresolvers import reverse

class TalkDetailTest(TestCase):
    
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name='Henrique Bastos', slug='henrique-bastos')
        self.resp = self.client.get(reverse('core:talk_detail', args=[1]))
    
    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')
    
    def test_talk_in_context(self):
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)
    
    def test_not_found(self):
        response = self.client.get(reverse('core:talk_detail', args=[0]))
        self.assertEqual(404, response.status_code)
    
    def test_html(self):
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/henrique-bastos/')
        self.assertContains(self.resp, 'Henrique Bastos')
