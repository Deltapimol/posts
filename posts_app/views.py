from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    posts = Post.objects.all()
    return render(request,'Posts/posts.html',{ 'posts': posts })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = displayComments(pk)
    return render(request,'Posts/detail.html',{ 'post': post, 'comments': comments })

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

def commentCreate(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentator = request.user
            comment.comment_datetime = timezone.now()
            comment.post = get_object_or_404(Post,pk=pk)
            comment.save()
            return render(request,'postdetails')
    else:
        form = CommentForm()
    context = { "form": form , "pk": pk}
    return render(request,'Posts/comment.html',context)

def displayComments(pk):
    comments = Comment.objects.filter(post_id=pk)
    return comments
    