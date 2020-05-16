from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE,)

    git_profile= models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True) 


    def __str__(self):
        return self.user.username

