from django.urls import path
from posts_app.views import createPost,displayPosts

urlpatterns = [
    path('',displayPosts,name='displayposts'),
    path('newpost/',createPost,name='createpost'),
    
]
