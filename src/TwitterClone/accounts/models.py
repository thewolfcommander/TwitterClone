from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from tweets.models import Tweet

User = get_user_model()

# Create your models here.
class UserProfileManager(models.Manager):
    use_for_related_fields = True
    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user = self.instance)
        except:
            pass
        return qs

    def toggle_follow(self, user, to_toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(user= user)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added = False
        else:
            user_profile.following.add(to_toggle_user)
            added=True
        return added

    def is_following(self, user, followed_by_user):
        user_profile, created = UserProfile.objects.get_or_create(user= user)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        return False



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    # user_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_name')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followed_by', blank=True, symmetrical=False)

    objects = UserProfileManager()
    def __str__(self):
        return str(self.following.all())

    # def get_user_name(self):
    #     users = self.objects.get('id')
    #     return users.user.username

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def get_follow_url(self):
        return reverse_lazy('accounts:follow', kwargs = {'username':self.user.username})

    def get_absolute_url(self):
        return reverse_lazy('accounts:profile',  kwargs = {'username':self.user.username})