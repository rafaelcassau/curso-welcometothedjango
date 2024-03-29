# coding: utf-8

from django.shortcuts import render, get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from django.http.response import HttpResponseRedirect
from eventex.subscriptions.models import Subscription
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

# Create your views here.

# def subscribe(request):
#     
#     if request.method == 'POST':
#         return create(request)
#     else:
#         return new(request)

class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    

def new(request):
    return render(
        request, 
        'subscriptions/subscription_form.html', 
        {'form': SubscriptionForm()}
    )

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})
    
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

# def detail(request, pk):
#     subscription = get_object_or_404(Subscription, pk=pk)
#     return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})

class SubscriptionDetail(DetailView):
    model = Subscription

    
