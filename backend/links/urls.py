from django.urls import include, path
from rest_framework import routers

from backend.links.views import TagViewSet

router = routers.DefaultRouter()

router.register(r"tags", TagViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
