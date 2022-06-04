from email.mime import image
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    