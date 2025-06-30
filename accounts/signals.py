import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models.user import CustomUser

@receiver(post_save, sender=CustomUser)
def generate_referral_code(sender, instance, created, **kwargs):
    if created and not instance.referral_code:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        instance.referral_code = code
        instance.save()
