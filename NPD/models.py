from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Police(models.Model):
    PID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80,blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=20,blank=True)
    password = models.CharField(max_length=30, blank=True)

