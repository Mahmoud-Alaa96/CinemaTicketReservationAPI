from django.db import models
from django.db .models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.views import Token
from django.conf import settings
from django.contrib.auth.models import User






# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    
    def __str__(self):
        return self.hall

class Reservation(models.Model):
    guest = models.ForeignKey("Guest", related_name="reservation", on_delete=models.CASCADE)
    movie = models.ForeignKey("movie", related_name="reservation", on_delete=models.CASCADE)


class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    title = models.TextField()



#auto add token to rest_framework_api 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created,  **kwargs):
    if created:
        Token.objects.create(user = instance)
