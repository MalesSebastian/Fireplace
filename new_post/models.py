from django.db import models
from django.utils import timezone

class Post(models):
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    time = timezone.now()

    def __unicode__(self):
        return self.title
# unfinished work


