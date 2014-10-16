# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from django.core.urlresolvers import reverse
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    
    def setUp(self):
        
        Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net',
            description='Passionate software developer!'
        )
        
        url = reverse('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
        self.resp = self.client.get(url)
        
    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')
    
    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Henrique Bastos')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://henriquebastos.net')
    
    def test_context(self):
        'Speaker must be in context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    
    def test_not_found(self):
        url = reverse('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
    
        