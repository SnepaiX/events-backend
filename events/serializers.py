from rest_framework import serializers
from .models import Event
from .models import EventImage


class EventImageSerializer(serializers.ModelSerializer):
    event = serializers.IntegerField()
    image = serializers.ImageField()
    preview = serializers.ImageField(read_only=True)

    class Meta:
        model = EventImage
        fields = [
            'id',
            'event',
            'image',
            'preview',
            'created_at',
        ]


class EventSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    place_name = serializers.CharField(
        source='place.name',
        read_only=True
    )
    images = EventImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'description',
            'publish_at',
            'start_at',
            'end_at',
            'rating',
            'status',
            'author',
            'place',
            'place_name',
            'created_at',
            'updated_at',
            'images',
        ]


class ImportXlsxSerializer(serializers.Serializer):
    file = serializers.FileField()
