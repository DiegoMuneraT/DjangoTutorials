from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=120)
    memo = models.TextField(blank=True)

    # Set to current time
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    # User who posted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title