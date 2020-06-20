from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone
from .models import Post, Comment, Reply
from .forms import PostForm, CommentForm, ReplyForm

class about(TemplateView):
    template_name = "about.html"    
    
class contact(TemplateView):
    template_name = "contact.html"
    
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
    comments = Comment.objects.filter(post_id=pk)
    replies = Reply.objects.filter(post_id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentator = request.user
            comment.comment_datetime = timezone.now()
            comment.post = get_object_or_404(Post,pk=pk)
            comment.save()
            form = CommentForm()
            return render(request,'Posts/detail.html',{'post':post, 'form':form ,'comments':comments, 'replies':replies})
    else:
        form = CommentForm()
    context = { 'post': post, 'comments': comments , "form": form , "pk": pk ,"replies":replies}
    return render(request,'Posts/detail.html',context)

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

def createReply(request, pk, pk2):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.post = get_object_or_404(Post, pk=pk)
            reply.comment = get_object_or_404(Comment , pk=pk2)
            reply.respondent = request.user
            reply.reply_datetime = timezone.now()
            reply.save()
            return redirect('postdetails',pk)
    else:
        form = ReplyForm()
    return render(request, 'Posts/reply.html',{ 'form': form, 'pk': pk ,'pk2':pk2})

def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('displayposts')

def deleteReply(request,pk,pk2,pk3):
    reply = Reply.objects.get(pk=pk3)
    reply.delete()
    return redirect('postdetails', pk)


    