from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    follower_since = models.DateField(default=timezone.now())

    class Meta:
        unique_together = ('user', 'follower')

    def __str__(self):
        return self.user.username + '< ---- >' + self.follower.username


class Following(models.Model):
    user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, on_delete=models.CASCADE)
    following_since = models.DateField(default=timezone.now())

    class Meta:
        unique_together = ('user', 'following_user')

    def __str__(self):
        return self.user.username + '< ---- >' + self.following_user.username


class Request(models.Model):
    user = models.ForeignKey(User, related_name='request_list', on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, related_name='requested_user_list', on_delete=models.CASCADE)
    request_date = models.DateField(default=timezone.now())
    request_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'requested_user')

    def __str__(self):
        return self.user.username + '------>' + self.requested_user.username
