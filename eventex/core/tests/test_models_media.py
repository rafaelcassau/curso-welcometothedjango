# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''

from django.test import TestCase
from eventex.core.models import Talk, Media

class MediaModelTest(TestCase):
    
    def setUp(self):
        t = Talk.objects.create(title='Talk',
        start_time='10:00')
        self.media = Media.objects.create(talk=t, kind='YT',
        media_id='QjA5faZF1A8', title='Video')

    def test_create(self):
        self.assertEqual(1, self.media.pk)
    
    def test_unicode(self):
        self.assertEqual('Talk - Video', unicode(self.media))