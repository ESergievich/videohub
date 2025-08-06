from django.contrib import admin

from videos.models import VideoFile, Video


class VideoFileInline(admin.TabularInline):
    """
    Inline admin configuration for VideoFile objects.

    Purpose:
        - Provides a tabular view of video files associated with a video.
    """
    model = VideoFile
    extra = 1


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Video model.

    Purpose:
        - Customizes how video objects are displayed, filtered,
          and managed in the Django admin panel.
    """

    list_display = ("name", "owner", "is_published", "total_likes", "created_at")
    list_filter = ("is_published",)
    search_fields = ("name", "owner__username")
    inlines = (VideoFileInline,)
