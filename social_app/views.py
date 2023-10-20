from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from social_app.models import UserProfile
from social_app.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )
