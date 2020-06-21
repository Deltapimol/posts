from django import forms
from django.conf import settings
from django.utils import timezone
from .models import Post, Comment, Reply, ReplyToReply

class PostForm(forms.ModelForm):
    
    title = forms.CharField(
                            widget = forms.TextInput(
                                    attrs={'class':'form-control','placeholder':'Title','size':95}
                                    )
                            )
    
    text = forms.CharField(
                            widget = forms.Textarea(
                                attrs = {
                                    'class': 'form-control','placeholder':'Text','rows':10,'cols':100
                                    }
                                )
                            )
    
    class Meta:
       model = Post
       fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    
    comment = forms.CharField(
                            widget = forms.Textarea(
                                attrs = {
                                    'class': 'form-control', 'rows': 3,'placeholder':'Comment'
                                    }
                                )
                            )

    class Meta:
        model = Comment
        fields = ('comment',)

class ReplyForm(forms.ModelForm):
    
    reply = forms.CharField(
                            widget = forms.Textarea(
                                attrs = {
                                    'class':'form-control','rows':3,'placeholder':'Reply',
                                }
                            )
    )
    
    class Meta:
        model = Reply
        fields = ('reply',)

class ReplyToReplyForm(forms.ModelForm):
    
    reply = forms.CharField(
                            widget = forms.Textarea(
                                attrs = {
                                    'class':'form-control','rows':3,'placeholder':'Reply',
                                }
                            )
    )
    
    class Meta:
        model = ReplyToReply
        fields = ('reply',) #Class based view?