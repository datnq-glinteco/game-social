from django.contrib import admin
from django.utils.html import format_html

from core.models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ["id", "post_file", "post", "created_at", "updated_at"]

    @admin.display
    def post_file(self, obj):
        file_html = format_html(
            '<img width = "200" height = "200" src="{}" alt="{}"/>',
            obj.file.url,
            obj.file.name,
        )
        return file_html
