from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.serializers import CustomUserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user
