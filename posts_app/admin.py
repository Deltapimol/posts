from django.contrib import admin
from .models import Post, Comment, Reply, Contact

# Registered model so records can be created or modified from the admin module
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Contact)

