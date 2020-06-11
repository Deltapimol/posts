from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone
from .models import Post
from .forms import PostForm

#class Index(TemplateView):
    #template_name = "index.html"

def createPost(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post_datetime = timezone.now()
            post.save()
            return redirect('displayposts')        
    else:
        post = PostForm()
    context = {'post': post}
    return render(request,'Posts/newpost.html',context)

def displayPosts(request):
    posts = Post.objects.filter()[:10]
    return render(request,'Posts/posts.html',{'posts': posts})
    