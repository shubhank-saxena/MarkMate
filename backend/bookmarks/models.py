from backend.authentication.models import User
from backend.core.models import MetaModel
from django.db import models


class BookmarkSource(MetaModel):
    """
    This model contains the data related to a Bookmark Source.

    Methods:
    str(self): Returns the source id.
    """

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark_source_user", blank=True, null=True, default=None)
    base_url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.id


class Bookmark(MetaModel):
    """
    This model contains the data related to a Bookmark.

    Methods:
    str(self): Returns the project id.
    """

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark_user")
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    metadata_image = models.URLField(blank=True, null=True, default=None)
    source = models.ForeignKey(BookmarkSource, on_delete=models.CASCADE, related_name="bookmark_source")
    after_thought = models.TextField(blank=True, null=True, default=None)
    is_later_read = models.BooleanField(default=False)
    reminder_time_for_later_read = models.DateTimeField(blank=True, null=True, default=None)


class BookmarkList(MetaModel):
    """
    This model contains the data related to a Bookmark List.

    Methods:
    str(self): Returns the list id.
    """

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark_list_user")
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_list")
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id


class BookmarkTag(MetaModel):
    """
    This model contains the data related to a Bookmark Tag.
    
    Methods:
    str(self): Returns the tag id.
    """

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark_tag_user")
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_tag")
    tag = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.id