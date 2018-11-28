from django.urls import path
from tweets.api.views import *
from .views import *

app_name = 'account-api'

urlpatterns = [
	path('<username>/feed/', TweetListAPIView.as_view(), name='list'),
	path('<username>/details/', UserDetailView.as_view(), name='user-detail'),



    # For APIs
    # path('twitter-clone/', TweetView.as_view(), name='twitter-api'),
]