from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    description = models.TextField(max_length=200)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, related_name='commie', on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
