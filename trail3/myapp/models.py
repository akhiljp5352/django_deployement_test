from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=300, null=True)
    constituency=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Voters(models.Model):
    slno=models.IntegerField()
    gender=models.CharField(max_length=10)
    religion=models.CharField(max_length=10)
    age=models.IntegerField()
    constituency=models.IntegerField()