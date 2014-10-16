# coding: utf-8

'''
Created on Apr 19, 2014

@author: rafael
'''
from django.conf.urls import patterns, url
from eventex.subscriptions.views import SubscriptionCreate, SubscriptionDetail

# urlpatterns = patterns('eventex.subscriptions.views',
#     url(r'^$', 'subscribe', name='subscribe'),
#     url(r'^(\d+)/$', 'detail', name='detail'),
# )

urlpatterns = patterns('',
    url(r'^$', SubscriptionCreate.as_view(), name='subscribe'),
    url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
)