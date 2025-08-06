from django.apps import AppConfig


class VideosConfig(AppConfig):
    """
    Application configuration for the videos app.

    Purpose:
        - Registers signals and performs startup configuration.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'
