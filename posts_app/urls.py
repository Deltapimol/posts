from django.urls import path
#from login_app import urls
from posts_app.views import createPost,displayPosts,postEdit,postDetail


urlpatterns = [
    
    path('',displayPosts,name='displayposts'),
    path(r'^newpost/$',createPost,name='createpost'),
    path(r'^postdetail/<int:pk>/$',postDetail,name='postdetails'),
    path('postdetail/<int:pk>/editdetails/',postEdit,name='editpost'),
    #path('comment/<int:pk>',)
   
]
