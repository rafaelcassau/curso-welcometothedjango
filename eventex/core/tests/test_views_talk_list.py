# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase
from eventex.core.models import Speaker, Talk

class TalkListTest(TestCase):
    
    def setUp(self):
        s = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net',
            description='Passionate software developer!'
        )
        
        t1 = Talk.objects.create(description=u'Descrição da palestra', title=u'Título da palestra', start_time='10:00')
        t2 = Talk.objects.create(description=u'Descrição da palestra', title=u'Título da palestra', start_time='13:00')
        
        t1.speakers.add(s)
        t2.speakers.add(s)
        
        self.resp = self.client.get(reverse('core:talk_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        'Template should be core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')
    
    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'10:00')
        self.assertContains(self.resp, u'13:00')
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/henrique-bastos/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Henrique Bastos', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)
        
    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.resp.context)
    
    def test_aftermoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)
        
        