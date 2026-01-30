from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'status',
        'start_at',
        'place',
        'author',
    )

    list_filter = (
        'status',
        'place',
    )

    search_fields = (
        'name',
        'description',
    )
