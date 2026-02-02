from django.db import models
from django.contrib.auth.models import User
from places.models import Place
from django.conf import settings
from PIL import Image


class Event(models.Model):

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_ARCHIVED, 'Archived'),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    publish_at = models.DateTimeField(
        verbose_name='Дата публикации'
    )

    start_at = models.DateTimeField(
        verbose_name='Начало мероприятия'
    )

    end_at = models.DateTimeField(
        verbose_name='Окончание мероприятия'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Автор'
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Место'
    )

    rating = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Рейтинг'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
        verbose_name='Статус'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-start_at']

    def __str__(self):
        return self.name


class EventImage(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='events/images/'
    )

    preview = models.ImageField(
        upload_to='events/previews/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.image and not self.preview:

            img = Image.open(self.image.path)

            min_side = min(img.size)

            left = (img.width - min_side) / 2
            top = (img.height - min_side) / 2
            right = (img.width + min_side) / 2
            bottom = (img.height + min_side) / 2

            img = img.crop((left, top, right, bottom))
            img.thumbnail((200, 200))

            preview_path = self.image.path.replace(
                'images',
                'previews'
            )

            img.save(preview_path)

            self.preview = preview_path.replace(
                str(settings.MEDIA_ROOT) + '/',
                ''
            )

            super().save(update_fields=['preview'])