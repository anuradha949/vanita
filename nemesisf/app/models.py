from django.db import models


# Create your models here.

class Login(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
  
   

class Signup(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
  