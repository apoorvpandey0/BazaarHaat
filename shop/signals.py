from .models import Shop,Approval
@receiver(post_save, sender=Shop())
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Approval.objects.create(user=instance)
