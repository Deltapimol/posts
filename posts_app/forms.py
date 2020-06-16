from django import forms
from django.conf import settings
from django.utils import timezone

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
       model = Post
       fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('comment',)

