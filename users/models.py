from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Purpose:
        - Allows adding additional fields and methods for user
          authentication and profile management.

    Usage:
        Used as AUTH_USER_MODEL in project settings.
    """

    def __str__(self):
        return self.username
