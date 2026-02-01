from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from django.utils import timezone

from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class EventViewSet(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = EventFilter

    search_fields = [
        'name',
        'place__name',
    ]

    ordering_fields = [
        'name',
        'start_at',
        'end_at',
    ]

    ordering = ['start_at']

    def get_permissions(self):

        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAdminUser()]

    def get_queryset(self):

        qs = super().get_queryset()

        user = self.request.user

        if not user.is_staff:
            qs = qs.filter(
                status=Event.STATUS_PUBLISHED,
                publish_at__lte=timezone.now()
            )

        return qs

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)
