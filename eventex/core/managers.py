# coding: utf-8

'''
Created on Apr 20, 2014

@author: rafael
'''
from django.db import models
from datetime import time

# class EmailContactManager(models.Manager):
# 
#     def get_query_set(self):
#         qs = super(EmailContactManager, self).get_query_set()
#         qs = qs.filter(kind='E')
#         return qs
# 
# class PhoneContactManager(models.Manager):
#     
#     def get_query_set(self):
#         qs = super(PhoneContactManager, self).get_query_set()
#         qs = qs.filter(kind='P')
#         return qs
# 
# class FaxContactManager(models.Manager):
#     
#     def get_query_set(self):
#         qs = super(FaxContactManager, self).get_query_set()
#         qs = qs.filter(kind='F')
#         return qs

class KindContactManager(models.Manager):

    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
    
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs


class PeriodManager(models.Manager):
    midday = time(12)
    
    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs
    
    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs