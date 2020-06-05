from django import forms
from django.conf import settings
from django.utils import timezone

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
       model = Post
       fields = ('title', 'text')

    # def save(self,commit=True):
    #     post = super(PostForm,self).save(commit=False)
    #     post.author = settings.USER_AUTH_MODEL
    #     post.title = self.cleaned_data['title']
    #     post.text = self.cleaned_data['title']
    #     post.post_datetime = timezone.now()
    #     if commit:
    #         post.save()
    #     return post
