from django.contrib import admin

from core.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "user",
        "count_attachments",
        "created_at",
        "updated_at",
    ]
    empty_value_display = "-empty-"

    actions_on_top = False
    actions_on_bottom = True

    @admin.display(empty_value="don't have attachments")
    def count_attachments(self, obj):
        return obj.attachments.count()
