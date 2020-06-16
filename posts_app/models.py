from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=200)
    text = models.TextField()
    post_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    commentator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    comment = models.CharField(blank=False,null=False,max_length=100)
    comment_datetime = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.comment

    
    
