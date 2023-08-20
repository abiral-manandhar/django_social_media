from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    description = models.TextField(max_length = 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    likes = models.ManyToManyField(User, related_name = "posts_likes")

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs = {'pk': self.pk})

    def get_like_url(self):
        return reverse('posts:like_toggle', kwargs = {'pk':self.pk})

    def get_like_api_url(self):
        return reverse('posts:like_api_toggle', kwargs={'pk': self.pk})


class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    post = models.ForeignKey(Post, null=False, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name= "comments", on_delete = models.CASCADE )
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    comment = models.TextField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)