# coding: utf-8

'''
Created on Apr 18, 2014

@author: rafael
'''
from django.test.testcases import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse

class SubscriptionFormTest(TestCase):
    
    def test_has_fields(self):
        'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
    
    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='ABC11111111')
        self.assertItemsEqual(['cpf'], form.errors)
    
    def test_cpf_has_11_digts(self):
        'CPF must have 11 digits.'
        form = self.make_validated_form(cpf='11')
        self.assertItemsEqual(['cpf'], form.errors)
    
    def test_email_is_optional(self):
        'Email is optional.'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
    
    def test_name_must_be_capitalized(self):
        'Name must be capitalized.'
        form = self.make_validated_form(name='RAFAEL cassau')
        self.assertEqual('Rafael Cassau', form.cleaned_data['name'])
    
    def test_must_inform_email_or_phone(self):
        'Email and Phone are optional, but one must be informed.'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
    
    def make_validated_form(self, **kwargs):
        data = dict(
                name='Rafael Cassau',
                cpf='11111111112',
                email='rafa_cassau@msn.com',
                phone_0='21',
                phone_1='111111111'
            )
        data.update(kwargs)
        
        form = SubscriptionForm(data)
        form.is_valid()
        
        return form
    
class SubscribePostTest(TestCase):
    
    def setUp(self):
        data = dict(
            name='Rafael Cassau',
            cpf='11111111111',
            email='rafa_cassau@msn.com',
            phone='11-111111111'
        )
        self.resp = self.client.post(reverse('subscriptions:subscribe'), data)
    
    def test_post(self):
        'Valid POST should redirect to /inscricao/1/.'
        self.assertEqual(302, self.resp.status_code)
    
    def test_save(self):
        'valid POST must saved.'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    
    def setUp(self):
        data = dict(
                name='Rafael Cassau',
                cpf='111111111112',
                email='rafa_cassau@msn.com',
                phone='11-111111111'
            )
        self.resp = self.client.post(reverse('subscriptions:subscribe'), data)
        
    def test_post(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.resp.status_code)
    
    def test_form_errors(self):
        'Form must contain errors.'
        self.assertTrue(self.resp.context['form'].errors)
    
    def test_dont_save(self):
        'Do not save data.'
        self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
    
    def test_template_has_non_field_errors(self):
        'Check if non_field_errors are shown in template.'
        invalid_data = dict(name='Rafael Cassau', cpf='12345678901')
        response = self.client.post(reverse('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<ul class="errorlist">')
