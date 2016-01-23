from django.db import models
from django.utils import timezone
import uuid
from django.core.urlresolvers import reverse


class Post(models.Model):

    title = models.CharField(max_length=100)
    post_text = models.TextField()
    #slug = models.SlugField(default=uuid.uuid1, unique=True)
    time = models.DateField(auto_now_add=True, editable=False)
    up_vote = models.IntegerField(default=0)
    category = models.TextField(default='')
    submitter = models.TextField(default='')

    def __init__(self, title, post_text, user, category):
        self.title = title
        self.post_text = post_text
        self.time = timezone.now()
        self.submitter = user
        self.category = category

  #  def get_absolute_url(self):
  #s      return reverse('post', args=[self.slug])

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

    def get_user(self):
        return self.submitter

    def get_category(self):
        return self.category

    def get_time(self):
        return self.time

    class Meta:
        get_latest_by = 'time'

