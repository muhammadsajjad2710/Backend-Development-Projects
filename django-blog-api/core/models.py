from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=40)
    body = models.CharField(max_length=500)
