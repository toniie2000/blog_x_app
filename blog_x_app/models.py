from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # author_id=models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title