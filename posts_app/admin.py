from django.contrib import admin
from .models import Post

# Registered model so records can be created or modified from the admin module
admin.site.register(Post)

