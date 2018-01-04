from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)