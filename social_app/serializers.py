from rest_framework import serializers

from social_app.models import (
    UserProfile,
    Like, Post, Comment
)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "post", "text", "created_at")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "owner", "content", "image", "created_at")


class PostListSerializer(serializers.ModelSerializer):
    num_likes = serializers.IntegerField(read_only=True)
    num_comments = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = (
        "id", "owner", "content", "num_likes", "num_comments", "created_at")


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True, source="post_comments")
    num_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "owner",
            "content",
            "image",
            "num_likes",
            "comments",
            "created_at",
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "user", "post")
        read_only_fields = ("id", "user")


class LikeDetailSerializer(LikeSerializer):
    post = PostSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = ("id", "post", "owner")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "owner",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "profile_picture",
            "bio",
            "followed",
            "created_at",
        )


class UserProfileListSerializer(UserProfileSerializer):
    profile_id = serializers.IntegerField(source="id", read_only=True)
    owner_id = serializers.IntegerField(source="owner.id", read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "profile_id",
            "owner_id",
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
        )


class UserProfileDetailSerializer(UserProfileSerializer):
    followed = UserProfileListSerializer(many=True, read_only=True)
    followers = UserProfileListSerializer(many=True, read_only=True)
    user_likes = LikeSerializer(many=True, source="owner.user_likes")

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "owner",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "profile_picture",
            "bio",
            "followed",
            "followers",
            "user_likes",
            "created_at",
        )
