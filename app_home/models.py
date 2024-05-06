from django.db import models
from django.contrib.auth.models import AbstractUser


class AboutInfo(models.Model):
    image = models.ImageField(upload_to='galerie/', default='default_profile.jpg')
    description = models.TextField(default='Description')
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance_available = models.BooleanField(default=False)

