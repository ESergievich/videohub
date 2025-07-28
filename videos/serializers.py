from rest_framework import serializers

from users.models import AppUser
from .models import Video, VideoFile


class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = ("file", "quality")


class VideoSerializer(serializers.ModelSerializer):
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
    username = serializers.CharField()
    likes_sum = serializers.IntegerField()

    class Meta:
        model = AppUser
        fields = ("username", "likes_sum")
