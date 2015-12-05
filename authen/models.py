from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
        user = models.OneToOneField(User, primary_key=True)
        points = models.IntegerField(default=1)
        level = models.IntegerField(default=1)

        def __init__(self, user):
            self.user = user

        def get_points(self):
            return self.points

        def get_level(self):
            return self.level


class Badge(models.Model):
        account = models.ForeignKey(Account, related_name="badges")
        name = models.TextField(default='')

        def __init__(self, account , name):
            self.account = account
            self.name = name




