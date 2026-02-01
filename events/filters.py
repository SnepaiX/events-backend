import django_filters

from .models import Event
from places.models import Place


class EventFilter(django_filters.FilterSet):

    start_at_from = django_filters.DateTimeFilter(
        field_name='start_at',
        lookup_expr='gte'
    )

    start_at_to = django_filters.DateTimeFilter(
        field_name='start_at',
        lookup_expr='lte'
    )

    end_at_from = django_filters.DateTimeFilter(
        field_name='end_at',
        lookup_expr='gte'
    )

    end_at_to = django_filters.DateTimeFilter(
        field_name='end_at',
        lookup_expr='lte'
    )

    rating_from = django_filters.NumberFilter(
        field_name='rating',
        lookup_expr='gte'
    )

    rating_to = django_filters.NumberFilter(
        field_name='rating',
        lookup_expr='lte'
    )

    place = django_filters.ModelMultipleChoiceFilter(
        field_name='place',
        queryset=Place.objects.all()
    )

    class Meta:
        model = Event
        fields = []
