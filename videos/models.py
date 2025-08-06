from django.db import models

from config import settings
from videos.querysets import VideoQuerySet


class Video(models.Model):
    """
    Represents a video entity in the database.

    Fields:
        - title, description, upload_date, etc. (depends on your model definition)

    Purpose:
        - Stores core video data and metadata.
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="videos"
    )
    is_published = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    total_likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    objects = VideoQuerySet.as_manager()

    def unpublish(self):
        self.is_published = False
        self.save(update_fields=["is_published"])


class VideoFile(models.Model):
    """
    Represents a file associated with a Video.

    Purpose:
        - Stores file metadata and a reference to the video file itself.

    Usage:
        Used for supporting multiple resolutions or file formats for a single video.
    """

    class Quality(models.TextChoices):
        """
        Represents video quality levels.
        """
        HD = "HD", "720p"
        FHD = "FHD", "1080p"
        UHD = "UHD", "4K"

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="files"
    )
    file = models.FileField(upload_to="videos/")
    quality = models.CharField(max_length=3, choices=Quality.choices)

    class Meta:
        unique_together = ("video", "quality")

    def __str__(self):
        return f"{self.video.name} ({self.quality})"


class Like(models.Model):
    """
    Represents a like action on a Video.

    Fields:
        - user: who liked the video
        - video: the video being liked

    Purpose:
        - Used to track user likes and calculate popularity statistics.
    """

    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("video", "user")
