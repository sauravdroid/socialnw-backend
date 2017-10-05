from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from Post.models import Post
from django.utils import timezone


# Create your models here.

class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.TextField()
    commented_at = models.DateField(default=timezone.now())

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.owner.get_full_name() + ' ---> ' + self.post.title
