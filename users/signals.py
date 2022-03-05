from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

from mailing.tasks import send_email
from django.forms.models import model_to_dict


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def send_email_to_user(sender, instance, created, **kwargs):
    if created:
        dict_user = model_to_dict(instance)
        send_email.delay(dict_user)
