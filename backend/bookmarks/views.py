from rest_framework import viewsets
from backend.bookmarks.models import BookmarkTag, Bookmark, BookmarkList, BookmarkSource
from backend.bookmarks.serializers import BookmarkTagSerializer, BookmarkSerializer, BookmarkListSerializer, BookmarkSourceSerializer
from rest_framework.permissions import IsAuthenticated


class BookmarkTagViewSet(viewsets.ModelViewSet):
    """This viewset provides the CRUD operations for the BookmarkTag model."""

    queryset = BookmarkTag.objects.all()
    serializer_class = BookmarkTagSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """Return the list of items for this view."""
        return BookmarkTag.objects.filter(created_by=self.request.user)


class BookmarkViewSet(viewsets.ModelViewSet):
    """This viewset provides the CRUD operations for the Bookmark model."""

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    queryset = Bookmark.objects.all()

    def get_queryset(self):
        """Return the list of items for this view."""
        return Bookmark.objects.filter(created_by=self.request.user)

class BookmarkListViewSet(viewsets.ModelViewSet):
    """This viewset provides the CRUD operations for the BookmarkList model."""

    queryset = BookmarkList.objects.all()
    serializer_class = BookmarkListSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """Return the list of items for this view."""
        return BookmarkList.objects.filter(created_by=self.request.user)

class BookmarkSourceViewSet(viewsets.ModelViewSet):
    """This viewset provides the CRUD operations for the BookmarkSource model."""

    queryset = BookmarkSource.objects.all()
    serializer_class = BookmarkSourceSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """Return the list of items for this view."""
        return BookmarkSource.objects.filter(created_by=self.request.user)
