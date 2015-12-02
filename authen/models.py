""""
from django.db import models
from django.contrib.auth.models import User


class UserModel(User):
    points = models.IntegerField(default=0)
    badges = models.

    def get_point(self):
        return self.points

    def get_badges(self):
        return self.badges

    def set_badges(self, badge):


    def set_point(self, point):
        self.points = self.points + point



            Work in progress 
"""

