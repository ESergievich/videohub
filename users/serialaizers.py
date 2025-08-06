from rest_framework import serializers
from .models import AppUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the AppUser model.

    Purpose:
        - Transforms AppUser model instances into JSON.
        - Validates input data for creating or updating user records.

    Usage:
        Used in APIs for user registration, profile retrieval,
        and profile update endpoints.
    """

    class Meta:
        model = AppUser
        fields = ('username',)
