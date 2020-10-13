from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars')
    # public_url = models.URLField(max_length=350, unique=True)

    def __str__(self):
        return self.user.username
