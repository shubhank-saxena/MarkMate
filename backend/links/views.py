from rest_framework import viewsets
from backend.links.models import BookmarkTag
from backend.links.serializers import TagSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class TagViewSet(viewsets.ModelViewSet):
    """This viewset provides the CRUD operations for the BookmarkTag model."""

    queryset = BookmarkTag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [
        AllowAny,
    ]

    def get_permissions(self):
        """Return the list of permissions that this view requires."""
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]