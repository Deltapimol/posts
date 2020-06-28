from django import forms
from django.conf import settings
from django.utils import timezone
from .models import Post, Comment, Reply,  Contact

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
                                    'class': 'form-control', 'rows': 3, 'placeholder':'Comment'
                                    }
                                )
                            )
    commentator = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class': 'form-control', 'placeholder': 'Name', 'size': 5
                                    }
                                )
                                )
    class Meta:
        model = Comment
        fields = ('comment','commentator')

class ReplyForm(forms.ModelForm):
    
    reply = forms.CharField(
                            widget = forms.Textarea(
                                attrs = {
                                    'class':'form-control','rows':3,'placeholder':'Reply',
                                }
                            )
    )
    
    respondent = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'Name','size': 5
                                    }
                                )
    )
    
    class Meta:
        model = Reply
        fields = ('reply','respondent')

class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'First Name','autofocus':True
                                    }
                                )
    )
    
    last_name = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'Last Name'
                                    }
                                )
    )
    
    email = forms.EmailField(
                            widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'Email'
                                    }
                            )
    )
    
    contact_no = forms.IntegerField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'Contact No.'
                                    }
                                )
    )
    
    location = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {
                                        'class':'form-control','placeholder':'Location'
                                    } 
                                )
    )
    
    
    class Meta:
        model = Contact
        fields = ('first_name','last_name','email','contact_no','location','reason_for_contact')
        widgets = {'reason_for_contact': forms.RadioSelect(
                                                        attrs = {
                                                            'class':'form-check-input','required':'required'
                                                            }
                                                        )}