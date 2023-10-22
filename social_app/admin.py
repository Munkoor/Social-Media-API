from django.contrib import admin
from social_app.models import (
    UserProfile,
    Post,
    Like,
    Comment,
)

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
