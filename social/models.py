from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(blank = True)
    
class Friends(models.Model):
    person1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person1')
    person2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person2')
    
class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length = 1024)
    