from django.urls import path
#from login_app import urls
from posts_app.views import createPost,displayPosts


urlpatterns = [
    
    path('',displayPosts,name='displayposts'),
    path('newpost/',createPost,name='createpost'),
    
]
