from django.db import models
from django.db.models import F, Q, Sum


class VideoQuerySet(models.QuerySet):
    """
    Custom queryset for Video model.

    Purpose:
        - Adds chainable helper methods for complex queries.

    Example methods:
        - .published(): filters only published videos
        - .popular(): filters by view count or likes
    """

    def published(self, user=None):
        """
        Filters only published videos.
        """
        if user is not None and user.is_authenticated:
            return self.filter(Q(is_published=True) | Q(owner=user))
        return self.filter(is_published=True)

    def statistics(self):
        """
        Returns a queryset with owner's username and total likes.
        """
        return (
            self.values("owner__username")
            .annotate(username=F("owner__username"), likes_sum=Sum("total_likes"))
            .values("username", "likes_sum")
            .order_by("-likes_sum")
        )
