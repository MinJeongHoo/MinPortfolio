from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True, default=0)
    phoneNum = models.CharField(null=True, default=None, max_length=10)
    career = models.IntegerField(null=True, default=0)
    introduce = models.TextField(null=True, max_length=500)
    profilePic = models.ImageField(null=True)

    def __str__(self):
        return self.username
