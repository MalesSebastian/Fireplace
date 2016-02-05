from django.db import models
from new_post.models import Post


class Comment(models.Model):
    text = models.CharField(default='', max_length=200)
    submitter = models.ForeignKey(Post, related_name="comments")
    shown_username = models.TextField(default='', max_length=20)
