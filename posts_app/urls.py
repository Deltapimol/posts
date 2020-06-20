from django.urls import path
from posts_app.views import createPost,displayPosts,postEdit,postDetail,createReply,deletePost,deleteReply


urlpatterns = [
    
    path('',displayPosts,name='displayposts'),
    path(r'^newpost/$',createPost,name='createpost'),
    path(r'^postdetail/<int:pk>/$',postDetail,name='postdetails'),
    path(r'^postdetail/<int:pk>/editdetails/$',postEdit,name='editpost'),
    path(r'^postdetail/<int:pk>/reply/<int:pk2>/$',createReply,name='reply'),
    path(r'^postdetail/<int:pk>/deletepost/$',deletePost,name='deletepost'),
    path(r'^postdetail/<int:pk>/reply/<int:pk2>/delete/<int:pk3>$',deleteReply,name='deletereply'),
    
]
