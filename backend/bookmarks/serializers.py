from rest_framework import serializers
from backend.bookmarks.models import (
    BookmarkTag,
    Bookmark,
    BookmarkSource,
    BookmarkList,
)

class BookmarkTagSerializer(serializers.ModelSerializer):
    """Serializer for Tag to handle request/response, data validation and conversion."""

    class Meta:
        """Define meta properties for the serializer."""

        model = BookmarkTag

        fields = "__all__"

        read_only_fields = ["id", "created_at", "updated_at"]

class BookmarkSourceSerializer(serializers.ModelSerializer):
    """Serializer for BookmarkSource to handle request/response, data validation and conversion."""

    class Meta:
        """Define meta properties for the serializer."""

        model = BookmarkSource

        fields = "__all__"

        read_only_fields = ["id", "created_at", "updated_at"]

class BookmarkListSerializer(serializers.ModelSerializer):
    """Serializer for BookmarkList to handle request/response, data validation and conversion."""

    class Meta:
        """Define meta properties for the serializer."""

        model = BookmarkList

        fields = "__all__"

        read_only_fields = ["id", "created_at", "updated_at"]

class BookmarkSerializer(serializers.ModelSerializer):
    """Serializer for Bookmark to handle request/response, data validation and conversion."""
    bookmark_tags = BookmarkTagSerializer(many=True, read_only=True)
    bookmark_source = BookmarkSourceSerializer(read_only=True)
    bookmark_list = BookmarkListSerializer(read_only=True)

    class Meta:
        """Define meta properties for the serializer."""

        model = Bookmark

        fields = "__all__"

        read_only_fields = ["id", "created_at", "updated_at"]
