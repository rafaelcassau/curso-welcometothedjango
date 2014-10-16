# coding: utf-8

'''
Created on Apr 19, 2014

@author: rafael
'''
from django.conf.urls import patterns, url
from eventex.core.views import HomeView, SpeakerDetail, TalkDetail

urlpatterns = patterns('eventex.core.views',
#     url(r'^$', 'home', name='home'),
#     url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail', name='speaker_detail'),
#     url(r'^palestras/(?P<pk>\d+)/$', 'talk_detail', name='talk_detail'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetail.as_view(), name='speaker_detail'),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    url(r'^palestras/(?P<pk>\d+)/$', TalkDetail.as_view(), name='talk_detail'),
)