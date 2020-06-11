from django.shortcuts import render, HttpResponse, redirect
from django.http import request
from django.contrib.auth import authenticate,login
from .forms import CreateUserForm

def userRegister(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('displayposts')
    else:
        form = CreateUserForm()
    context = { 'form': form}
    return render(request,'userRegister.html',context)
