from rest_framework import serializers
from django.urls import reverse_lazy
from accounts.models import UserProfile, UserProfileManager
from accounts.views import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
	total_user = serializers.SerializerMethodField()
	# follower_user = serializers.SerializerMethodField()
	url = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ['username', 'email', 'total_user', 'url']
		extra_kwargs = {'email': {'write_only':True}}

	def get_total_user(self, obj):
		user_count = UserProfile.objects.all().count()
		return user_count

	# def get_follower_user(self, obj):
	# 	follower_counting = UserProfile.objects.get('username')
	# 	return follower_counting.items().count()

	def get_url(self, obj):
		return reverse_lazy('accounts:profile', kwargs={'username' : obj.username})

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['following']

# class UserFollowerSerial
