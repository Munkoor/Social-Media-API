from django.urls import path, include
from rest_framework import routers

from social_app.views import UserProfileViewSet

router = routers.DefaultRouter()


router.register("profiles", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "social-media"
