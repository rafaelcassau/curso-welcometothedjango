# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from django.template import Context, Template

class YoutubeTagTest(TestCase):
    
    def setUp(self):
        context = Context({'ID': 1})
        template = Template('{% load youtube %}{% youtube ID %}')
        self.content = template.render(context)
    
    def test_output(self):
        self.assertIn('<object', self.content)
        self.assertIn('/1', self.content)