from django.db.models.signals import post_save
from django.dispatch import receiver
from baskets.models import Basket


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(user=instance)