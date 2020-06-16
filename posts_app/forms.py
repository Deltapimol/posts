from django import forms
from django.conf import settings
from django.utils import timezone

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
       model = Post
       fields = ('title', 'text')

