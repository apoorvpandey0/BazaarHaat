import os

from django.dispatch import receiver
from django.db import models

from .models import Slide

@receiver(models.signals.post_delete, sender=Slide)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            # print("File deleted")
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Slide)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False
    try:
        old_file = Slide.objects.get(pk=instance.pk).image
    except Slide.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            # print("File deleted on change")
            os.remove(old_file.path)
