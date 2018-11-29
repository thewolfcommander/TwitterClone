from django.urls import path
from tweets.api.views import *
from .views import *

app_name = 'account-api'

urlpatterns = [
    path('<username>/feed/', TweetListAPIView.as_view(), name='list'),
    path('<username>/following/', UserDetailView.as_view(), name='user-detail'),
    path('<username>/followers/', UserDetailFollowerView.as_view(), name='user-follower'),



    # For APIs
    # path('twitter-clone/', TweetView.as_view(), name='twitter-api'),
]