from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

app_name = 'tweets'

urlpatterns = [
    path('', RedirectView.as_view(url='/')),
    path('tweet-details/<pk>/', tweet_detail_view, name='tweet-detail'),
    path('tweet-create/', TweetCreateView.as_view(), name='tweet-create'),
    path('tweet-details/<pk>/update/', TweetUpdateView.as_view(), name='tweet-update'),
    path('tweet-details/<pk>/delete/', TweetDeleteView.as_view(), name='tweet-delete'),

    # For APIs
    # path('twitter-clone/', TweetView.as_view(), name='twitter-api'),
]