from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Application configuration class for the user management app.

    Purpose:
        - Registers signals, performs initialization logic, and
          configures app settings when the 'users' app is loaded.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
