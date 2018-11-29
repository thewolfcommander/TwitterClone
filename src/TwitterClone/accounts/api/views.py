from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


from .serializers import *
from accounts.models import *
from accounts.views import *

class UserDetailView(APIView):
    def get(self, request, username, format=None):
        user_det1 = User.objects.all().order_by('id')
        user_det2 = UserProfile.objects.all().order_by('id')
        serializer1 = UserProfileFollowerSerializer(user_det1, many=True)
        serializer2 = UserProfileFollowingSerializer(user_det2, many=True)
        serializer = serializer1.data + serializer2.data
        return Response(serializer)

    def post(self, request, username, format=None):
        serializer = UserProfileFollowingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailFollowerView(APIView):
    def get(self, request, username, format=None):
        user_det1 = User.objects.all().order_by('id')
        # user_det2 = UserProfile.objects.all().order_by('id')
        serializer1 = UserProfileFollowerSerializer(user_det1, many=True)
        # serializer2 = UserProfileFollowingSerializer(user_det2, many=True)
        # serializer = serializer1.data + serializer2.data
        return Response(serializer1.data)

    def post(self, request, username, format=None):
        serializer = UserProfileFollowerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
