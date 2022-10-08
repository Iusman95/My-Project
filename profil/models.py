from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(blank=True)

    
class Follower(models.Model):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField('user.User', blank=True)
    following = models.ManyToManyField('user.User', blank=True)
