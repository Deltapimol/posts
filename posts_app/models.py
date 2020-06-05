from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=200)
    text = models.TextField()
    post_datetime = models.DateTimeField(null=True)

    #def post(self):
       #self.post_datetime = timezone.now()
       #self.save()
    
    def __str__(self):
        return self.title
    
    
