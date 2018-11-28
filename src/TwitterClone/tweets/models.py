from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse_lazy

# Validations
def validate_content(value):
    content = value
    if content == 'abc':
        raise ValidationError('Content cannot be ABC')
    return value


# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default= 1, on_delete = models.CASCADE)
    content = models.CharField(max_length = 140, validators = [validate_content])
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse_lazy('tweets:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-updated', 'content']

    # def clean(self, *args, **kwargs):
    #   content = self.content
    #   if content == 'abc':
    #       raise ValidationError('Content cannot be ABC')
    #   return super(Tweet, self).clean(*args, **kwargs)