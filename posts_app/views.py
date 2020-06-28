from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib import messages
from posts import urls
from .models import Post, Comment, Reply , ReplyToReply, Contact
from .forms import PostForm, CommentForm, ReplyForm, ReplyToReplyForm, ContactForm

class about(TemplateView):
    template_name = "about.html"    
    
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.datetime = timezone.now()
            contact.save()
            messages.success(request, 'Contact details submitted successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    context = { 'form': form }
    return render(request,'contact.html',context)
        
def createPost(request):                            # For creating new post

    if request.method == 'POST':                    # If request is POST, save the form data else generate a blank form
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

def displayPosts(request):                          # For displaying all posts
    posts_list = Post.objects.all()  
    paginator = Paginator(posts_list,5)             # Paginator for allowing 5 posts on a page
    
    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1
    
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):         
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'Posts/posts.html',{ 'posts': posts, })

def postDetailAndComment(request, pk):              # view for generating template to display post and its comments and details. Also generates a form for comment submission
    post = get_object_or_404(Post, pk=pk)           # get post, comments and replies using pk of post
    comments = Comment.objects.filter(post_id=pk)  
    replies = Reply.objects.filter(post_id=pk)
    
    reply_ids = []
    for reply in replies:
        reply_ids.append(reply.pk)
    
    RepliesToReplies = ReplyToReply.objects.filter(reply_id__in=reply_ids) #????
    
    if request.method == "POST":
        form = CommentForm(request.POST)             # If the request is POST,save comment data and render template again.
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_datetime = timezone.now()
            comment.post = get_object_or_404(Post,pk=pk)
            comment.save()
            form = CommentForm()                     # Clear the form after comment submission
            return render(request,'Posts/detail.html',{'post':post, 'form':form, 'comments':comments, 'replies':replies, 'RepliesToReplies':RepliesToReplies })
    else:
        form = CommentForm()    
    context = { 'post': post, 'comments': comments, "form": form, "pk": pk, "replies":replies, 'RepliesToReplies':RepliesToReplies}
    return render(request,'Posts/detail.html',context)

def postEdit(request, pk):                          # View for post editing.
    post = get_object_or_404(Post, pk=pk)           # Fetch the post using the post id.
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post) # Passing the instance of post that needs editing.
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.post_datetime = timezone.now()
            post.save()
            return redirect('postdetails',pk)       # Redirect to the page again with the edited post.
    else:
        form = PostForm(instance=post)              # In case of GET request, fetch the post instance for editing.
    return render(request,'Posts/edit.html',{ 'form': form , 'pk': pk })

def createReply(request, **kwargs):
    
    ReplyFlag = bool()                              # Boolean variable to decide what form field to display on template.
    pk = kwargs['pk']                               # Fetching primary keys from the url.
    pk2 = kwargs['pk2']
    
    if "pk3" in kwargs:                             # Check if there is a primary key for a reply. This will have value only when user replies to a reply via its url.
        pk3 = kwargs['pk3']         
        if request.method == 'POST':                # If there is a reply primary key, render a ReplyToReply form depending on the type of request.
            Form = ReplyToReplyForm(request.POST)
            if Form.is_valid:
                reply = Form.save(commit=False)
                #reply.post = get_object_or_404(Post, pk=pk)
                #reply.comment = get_object_or_404(Comment , pk=pk2)
                reply.reply = get_object_or_404(Reply, pk=pk3)
                reply.reply_datetime = timezone.now()
                reply.save()
                return redirect('postdetails',pk)
        else:
            Form = ReplyToReplyForm()
        context = { 'form': Form, 'pk':pk, 'pk2':pk2, 'pk3':pk3, 'ReplyFlag':True } # Context dictionary when ReplyToReply Form is requested. ReplyFlag set to True.
        
    else:
        if request.method == 'POST':                # In case of a reply to a comment. There is no 3rd primary key passed via the url. Thus here it renders a Reply Form depending on the type of request.
            Form = ReplyForm(request.POST)
            if Form.is_valid():
                reply = Form.save(commit=False)
                reply.post = get_object_or_404(Post, pk=pk)
                reply.comment = get_object_or_404(Comment, pk=pk2)
                reply.reply_datetime = timezone.now()
                reply.save()
                return redirect('postdetails',pk) 
        else:
            Form = ReplyForm()
        context = { 'form':Form, 'pk':pk, 'pk2':pk2, 'ReplyFlag':False }    # Context dictionary when Reply Form is requested. ReplyFlag set to False
    return render(request,'Posts/reply.html', context)

def deletePost(request, pk):    
    post = Post.objects.get(pk=pk)                  # Fetch the post which needs to be deleted 
    post.delete()
    return redirect('displayposts')

def deleteComment(request,pk,pk2):
    comment = Comment.objects.get(pk=pk2)           # Fetch the comment which needs to be deleted 
    comment.delete()
    return redirect('postdetails', pk)

def deleteReply(request,pk,pk2,pk3):
    reply = Reply.objects.get(pk=pk3)               # Fetch the reply which needs to be deleted
    reply.delete()
    return redirect('postdetails', pk)




    