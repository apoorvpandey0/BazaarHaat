from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user           = models.OneToOneField(
                        User,
                        on_delete=models.CASCADE
    )
    image          = models.ImageField(
                        _('Profile Picture'),
                        default='default.png',
                        upload_to='profile_pics',
                        help_text=_('Designates the users Profile picture.')
    )
    address_line1  = models.CharField(
                        _('Address line 1'),
                        max_length=100,
                        help_text=_('Designates the users Address line1.')
    )
    address_line2  = models.CharField(
                        _('Address line 2'),
                        max_length=100,
                        help_text=_('Designates the users Address line 2.')
    )
    pincode        = models.CharField(
                        _('Pincode'),
                        max_length=6,
                        help_text=_('Designates the users PINCODE.')
    )
    contactno      = models.CharField(max_length=10,default=1234567890)
    is_seller      = models.BooleanField(
                        _('Seller status'),
                        default=False,
                        help_text=_('Designates whether the user has a seller account or not.')
    )

    def __str__(self):
        return f'{self.user.username}'#.format(a="Seller" if self.is_seller==True else "Regular")
    def get_username(self):
        return self.user.username
    def get_email(self):
        return self.user.email
    def get_fullname(self):
        return self.user.get_full_name()

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width >300 :
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# #Signals part can be used alternatively for signals.py
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# #        print("Create_profile function executed!")
#
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
# #    print("Save_profile function executed!")
#
# post_save.connect(create_profile,sender=User)
# post_save.connect(save_profile,sender=User)
