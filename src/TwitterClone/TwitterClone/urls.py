from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tweets.views import tweet_list_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', tweet_list_view, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('feed/', include('tweets.urls', namespace='tweets')),

    path('api/feed/', include('tweets.api.urls', namespace='tweet-api')),
    path('api/', include('accounts.api.urls', namespace='account-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

