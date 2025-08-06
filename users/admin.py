from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    """
    Custom Django admin configuration for the AppUser model.

    Extends:
        UserAdmin: Django's built-in admin class for managing users.

    Purpose:
        - Customizes the display, search, and management of AppUser data
          in the Django admin panel.
    """
