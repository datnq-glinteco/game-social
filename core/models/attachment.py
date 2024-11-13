from django.db import models


class Attachment(models.Model):
    file = models.FileField(upload_to="attachments/")
    post = models.ForeignKey(
        "core.Post", related_name="attachments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.file.name
