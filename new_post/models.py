from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    time = timezone.now()
    upvote = models.IntegerField()
    downvote = models.IntegerField()

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.post_text = text

    def get_upvote (self):
        return self.upvote

    def get_downvote (self):
        return self.downvote
# unfinished work


