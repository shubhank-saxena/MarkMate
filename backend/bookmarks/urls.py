from django.urls import include, path
from rest_framework import routers

from backend.bookmarks.views import BookmarkViewSet, BookmarkTagViewSet, BookmarkListViewSet, BookmarkSourceViewSet

router = routers.DefaultRouter()

router.register(r"bookmark", BookmarkViewSet)
router.register(r"bookmark_tag", BookmarkTagViewSet)
router.register(r"bookmark_list", BookmarkListViewSet)
router.register(r"bookmark_source", BookmarkSourceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
