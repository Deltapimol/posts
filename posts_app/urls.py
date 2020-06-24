from django.urls import path
from posts_app.views import createPost,displayPosts,postEdit,postDetailAndComment,createReply,replyToReply,deletePost,deleteComment,deleteReply,contact

urlpatterns = [
    
    path('',displayPosts,name='displayposts'),
    path(r'^newpost/$',createPost,name='createpost'),
    path(r'^postdetail/<int:pk>/$',postDetailAndComment,name='postdetails'),
    path(r'^postdetail/<int:pk>/editdetails/$',postEdit,name='editpost'),
    path(r'^postdetail/<int:pk>/reply/<int:pk2>/$',createReply,name='reply'),
    path(r'^postdetail/<int:pk>/deletepost/$',deletePost,name='deletepost'),
    path(r'^postdetail/<int:pk>/deletecomment/<int:pk2>$',deleteComment,name='deletecomment'),
    path(r'^postdetail/<int:pk>/reply/<int:pk2>/delete/<int:pk3>$',deleteReply,name='deletereply'),
    path(r'^postdetail/<int:pk>/reply/<int:pk2>/reply/<int:pk3>$',replyToReply,name='replytoreply'),
    path(r'^contact/$',contact,name='contact'),
    
]
