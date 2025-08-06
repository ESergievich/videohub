from rest_framework import serializers

from users.models import AppUser
from .models import Video, VideoFile


class VideoFileSerializer(serializers.ModelSerializer):
    """
    Serializer for the VideoFile model.

    Purpose:
        - Transforms VideoFile data to/from JSON.
        - Typically used as a nested serializer inside VideoSerializer.
    """

    class Meta:
        model = VideoFile
        fields = ("file", "quality")


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.

    Purpose:
        - Converts Video model instances into JSON format.
        - Can include related files or statistics for detailed API responses.
    """

    owner = serializers.CharField(source="owner.username", read_only=True)
    files = VideoFileSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = (
            "pk",
            "owner",
            "name",
            "total_likes",
            "created_at",
            "files",
        )


class StatisticsSerializer(serializers.ModelSerializer):
    """
    Serializer for video statistics.

    Purpose:
        - Provides a structured representation of likes.
    """

    username = serializers.CharField()
    likes_sum = serializers.IntegerField()

    class Meta:
        model = AppUser
        fields = ("username", "likes_sum")
