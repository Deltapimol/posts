from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone
from .models import Post
from .forms import PostForm

class about(TemplateView):
    template_name = "about.html"    
    
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
    return render(request,'Posts/posts.html',{'posts': posts })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'Posts/detail.html',{ 'post': post })

def postEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.post_datetime = timezone.now()
            post.save()
            return redirect('postdetails',pk)
    else:
        form = PostForm(instance=post)
    return render(request,'Posts/edit.html',{ 'form': form , 'pk': pk })
    