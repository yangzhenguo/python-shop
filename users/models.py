from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=128)
    email=models.CharField(max_length=30)
    postname=models.CharField(max_length=20, default='')
    postaddress=models.CharField(max_length=100, default='')
    zipcode=models.CharField(max_length=10, default='')
    postphone=models.CharField(max_length=11, default='')
