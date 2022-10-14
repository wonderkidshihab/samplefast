# import django permissions and create permissions for user
# Compare this snippet from ecommercebackend/user/models.py:
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.
