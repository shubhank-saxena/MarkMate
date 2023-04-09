from rest_framework import serializers
from backend.links.models import (
    BookmarkTag,
)

class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag to handle request/response, data validation and conversion."""

    class Meta:
        """Define meta properties for the serializer."""

        model = BookmarkTag

        fields = "__all__"