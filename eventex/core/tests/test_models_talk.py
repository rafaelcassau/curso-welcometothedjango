# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''

from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    
    def setUp(self):
        self.talk = Talk.objects.create(
        title=u'Introdução ao Django',
        description=u'Descrição da palestra.',
        start_time='10:00')
    
    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))
        
    def test_speakers(self):
        'Talk has many Speakers and vice-versa.'
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            url='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())
    
    def test_period_manager(self):
        'Talk default manager must be instance of PeriodManager.'
        self.assertIsInstance(Talk.objects, PeriodManager)