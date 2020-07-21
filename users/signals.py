#This is the signal that will be sent
from django.db.models.signals import post_save

#This is the object which will send the signal
from django.contrib.auth.models import User

#This will receive the signal
from django.dispatch import receiver

#We need this to perform operations on profiles table
from .models import Profile

#This function creates new profile for each user created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Create_profile function executed!")

#This function saves those newly created profiles
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("Save_profile function executed!")
