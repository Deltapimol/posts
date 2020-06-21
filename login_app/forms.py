from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    
    first_name = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {'class':'form-control','placeholder':'First Name','autofocus':True}
                                )
                                )
    last_name = forms.CharField(
                                widget = forms.TextInput(
                                    attrs = {'class':'form-control','placeholder':'Last Name'}
                                )
                                )
    email = forms.EmailField(
                            widget = forms.EmailInput(
                                attrs = {'class':'form-control','placeholder':'Email'}
                            )
                            )
    username = forms.CharField(
                                widget = forms.TextInput(
                                 attrs = {'class':'form-control','placeholder':'Username',}   
                                )
                            )
    password1 = forms.CharField(
                                widget = forms.PasswordInput(
                                    attrs = {'class':'form-control','placeholder':'Password'}
                                )
                                )
    password2 = forms.CharField(
                                widget = forms.PasswordInput(
                                   attrs = {'class':'form-control','placeholder':'Confirm Password'} 
                                )
                                )
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')
    
    def save(self,commit=True):
        user = super(CreateUserForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        
        if commit:
            user.save()
        return user



