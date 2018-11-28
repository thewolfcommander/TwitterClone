from django.db import models
# from django.conf import settings
# from django.core.validators import RegexValidator
# from django.views import generic
# import random

# User = settings.AUTH_USER_MODEL

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
#     image = models.ImageField(upload_to = 'profile')
#     full_name = models.CharField(max_length = 80)
#     ref_code = random.randint(51651651, 51651651161)
#     balance = models.DecimalField(max_digits = 20, decimal_places = 2, default = 0.00)
#     credit_amount = models.DecimalField(max_digits = 20, decimal_places = 2, default = 0.00)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
