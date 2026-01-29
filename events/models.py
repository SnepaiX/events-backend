from django.conf import settings
from django.db import models

from places.models import Place


class Event(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    publish_at = models.DateTimeField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        related_name='events',
    )

    rating = models.PositiveSmallIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name