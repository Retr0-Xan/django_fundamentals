from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner= models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None) #on delete tells db how to handle data when user/relationship is deleted. Cascade means, if user gets
    #deleted, all posts will be deleted.

    def __str__(self):
        return self.title