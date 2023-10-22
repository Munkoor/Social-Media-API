from django.urls import path, include
from rest_framework import routers

from social_app.views import UserProfileViewSet, LikeViewSet, PostViewSet

router = routers.DefaultRouter()


router.register("profiles", UserProfileViewSet)
router.register("likes", LikeViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "social-media"
