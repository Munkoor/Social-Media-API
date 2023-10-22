from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from social_app.models import UserProfile, Like, Post
from social_app.serializers import (
    UserProfileSerializer,
    UserProfileListSerializer,
    UserProfileDetailSerializer,
    LikeSerializer,
    PostSerializer,
    PostListSerializer,
    PostDetailSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        last_name = self.request.query_params.get("last_name")

        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer

        if self.action == "retrieve":
            return UserProfileDetailSerializer

        return UserProfileSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, pk=self.request.data["post"])
        if self.request.data.get("like"):
            already_liked = Like.objects.filter(
                post=post_instance, owner=self.request.user
            ).exists()
            if already_liked:
                raise ValidationError(
                    {"message": "You have already liked this post"}
                )
            else:
                serializer.save(post=post_instance, owner=self.request.user)
        elif self.request.data.get("unlike"):
            Like.objects.filter(
                post=post_instance, owner=self.request.user
            ).delete()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        content = self.request.query_params.get("content")
        user = self.request.query_params.get("user")
        queryset = self.queryset
        if content:
            queryset = queryset.filter(content__icontains=content)

        if user:
            queryset = queryset.filter(owner_id=user)

        return queryset.distinct()
