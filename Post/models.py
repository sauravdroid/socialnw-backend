from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    cover_pic = models.FileField()
    subheader = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title + '<--->' + self.owner.username


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    like_status = models.BooleanField(default=False)
    liked_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user.get_full_name() + ' ---> ' + self.post.title + ' ----> ' + str(self.like_status)
