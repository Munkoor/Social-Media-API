import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def image_file_path(instance, filename: str) -> str:
    _, extension = os.path.splitext(filename)
    return os.path.join(
        "uploads/images/",
        f"{slugify(instance.user)}-{uuid.uuid4()}{extension}"
    )


class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True)
    gender = models.CharField(
        max_length=63, choices=GenderChoices.choices, null=True
    )
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to=image_file_path, blank=True
    )
    followed = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="user_comments")
    content = models.TextField()
    image = models.ImageField(upload_to=image_file_path,
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_comments")
    text = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

