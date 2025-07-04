from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
        
from django.db import models

def upload_location(instance, filename):
    return f'repositories/{instance.rep_id}/{filename}'

class Repository(models.Model):
    rep_id = models.CharField(max_length=100)
    rep_name = models.CharField(max_length=100)
    rep_des = models.TextField()
    file = models.FileField(upload_to='repositories/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed to ForeignKey


    def __str__(self):
        return self.rep_name


from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groupid = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db import models  

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)  # Allow null and blank
    hobbies = models.TextField(null=True, blank=True)  # Allow null and blank
    skill1 = models.CharField(max_length=255, null=True, blank=True)
    progress1 = models.IntegerField(null=True, blank=True)
    skill2 = models.CharField(max_length=255, null=True, blank=True)
    progress2 = models.IntegerField(null=True, blank=True)
    skill3 = models.CharField(max_length=255, null=True, blank=True)
    progress3 = models.IntegerField(null=True, blank=True)
 
  
def __str__(self):  
      return f"{self.user.username}'s Profile" 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    groupid = models.CharField(max_length=255, default=123)

    def __str__(self):
        return f"{self.user.username} - {self.groupid}"