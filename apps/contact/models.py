# apps/contact/models.py

# Django modules
from django.db import models

# Django locals

# Create your models here.

# Contact model
class Contact(models.Model):
    contact_username = models.CharField(max_length=50)
    contact_password = models.CharField(max_length=50)
    contact_avatar = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_telp = models.CharField(max_length=50)