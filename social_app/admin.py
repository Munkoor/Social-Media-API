from django.contrib import admin
from social_app.models import (
    UserProfile,
    Post,
    Like,
    Comment,
    Follow,
)

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follow)
