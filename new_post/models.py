from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    time = timezone.now()
    up_vote = models.IntegerField(default= 0)
   # category = models.TextField()
    #submitter = models.TextField(default="")

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text
        self.time = timezone.now()

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.post_text = text

    def set_category(self, category):
        self.category = category

    def get_up_vote (self):
        return self.up_vote

    def get_title(self):
        return self.title

    def get_text(self):
        return self.post_text

# unfinished work

