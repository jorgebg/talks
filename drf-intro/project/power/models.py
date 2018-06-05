from django.contrib.auth.models import User
from django.db import models


class Ring(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Ring of {}".format(self.title)
