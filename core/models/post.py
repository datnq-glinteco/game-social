from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(
        max_length=100000, default="", blank=True, null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def attachments(self):
        return self.attachments

    def __str__(self) -> str:
        return self.title
