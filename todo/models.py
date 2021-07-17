from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    memo = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)        # not editable
    completed_at = models.DateTimeField(null=True, blank=True)  # not required
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
