from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.shortcuts import render

from .serializers import UserDisplaySerializer, UserProfileSerializer
from accounts.models import *

class UserDetailView(APIView):
	def get(self, request, username, format=None):
		user_det = UserProfile.objects.all()
		serializer = UserProfileSerializer(user_det, many=True)
		return Response(serializer.data)

	def post(self, request, username, format=None):
		serializer = UserProfileSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

# class UserDisplayView(APIView):
# 	def get(self, request, username, format=None):
# 		user_det = UserProfile.objects.all()
# 		serializer = UserDisplaySerializer(user_det, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, username, format=None):
# 		serializer = UserDisplaySerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)