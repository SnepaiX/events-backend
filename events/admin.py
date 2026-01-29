from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'publish_at', 'start_at')
    list_filter = ('status',)
    search_fields = ('name',)
