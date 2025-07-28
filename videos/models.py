from django.db import models

from config import settings
from videos.querysets import VideoQuerySet


class Video(models.Model):
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
    class Quality(models.TextChoices):
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
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("video", "user")
