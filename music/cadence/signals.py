from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from cadence.models import Userprofile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Userprofile.objects.create(user=instance)
        print("Profile Created")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.userprofile.save()
        print("profilie updated")
