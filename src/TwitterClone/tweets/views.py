from django.shortcuts import render, get_object_or_404
from django.forms.utils import ErrorList
from .models import Tweet
from accounts.models import UserProfile
from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# For APIs
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from . import serializers


# Create your views here.
def tweet_list_view(request):
    all_tweet_list = Tweet.objects.all().order_by('-updated')
    create_form = TweetModelForm()
    create_url = reverse_lazy('tweets:tweet-create')
    all_users = UserProfile.objects.all().order_by('following')
    context = {
        'all_tweet_list' : all_tweet_list,
        'create_form' : create_form,
        'create_url' : create_url,
        'all_users': all_users,
    }
    return render(request, 'tweets/tweet_list.html', context)

def tweet_detail_view(request, pk=None, *args, **kwargs):
    obj = Tweet.objects.get(pk=pk)
    return render(request, 'tweets/tweet_detail.html', {'obj':obj,})


# class TweetDetailView(DetailView):
#     queryset = Tweet.objects.all()
#     template_name = 'tweets/tweet_detail.html'

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/feed/tweet-create/'
    # login_url = '/admin/'

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url = '/feed/'
    template_name = 'tweets/update_view.html'


class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    queryset = Tweet.objects.all()
    success_url = reverse_lazy('tweets:tweet-list')
    template_name = 'tweets/delete_confirm.html'

