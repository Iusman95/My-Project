from django.db import models



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = models.TextField(blank=True)

    
class UserFollowing(models.Model):
    user_id = models.ForeignKey("user.User", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("user.User", related_name="followers",  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
