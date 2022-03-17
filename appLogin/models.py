from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profiles')
    profile_pics = models.ImageField(upload_to='profile_pics')


