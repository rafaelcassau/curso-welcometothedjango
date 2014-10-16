# coding: utf-8

from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker
from django.http.response import HttpResponse
from datetime import time
from eventex.core.models import Talk
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# def home(request):
# 	return render(request, 'index.html')

class HomeView(TemplateView):
	template_name = 'index.html'

# def speaker_detail(request, slug):
# 	speaker = get_object_or_404(Speaker, slug=slug)
# 	context = {'speaker': speaker}
# 	return render(request, 'core/speaker_detail.html', context)

class SpeakerDetail(DetailView):
	model = Speaker

def talk_list(request):
	
	context = {
		'morning_talks': Talk.objects.at_morning(),
		'afternoon_talks': Talk.objects.at_afternoon()
	}
	return render(request, 'core/talk_list.html', context)

# def talk_detail(request, pk):
# 	talk = get_object_or_404(Talk, pk=pk)
# 	context = {
# 				'talk': talk,
# 				'slides': talk.media_set.filter(kind='SL'),
# 				'videos': talk.media_set.filter(kind='YT'),
# 			}
# 	return render(request, 'core/talk_detail.html', context)

class TalkDetail(DetailView):
	model = Talk
