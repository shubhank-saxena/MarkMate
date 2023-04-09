# from django.contrib.auth.models import User
from backend.core.models import MetaModel
from django.db import models


class Bookmark(MetaModel):
    """
    This model contains the data related to a Bookmark.

    Methods:
    str(self): Returns the project id.
    """

    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    metadata_image = models.URLField(blank=True, null=True, default=None)

class BookmarkAfterThought(MetaModel):
    """
    This model contains the data related to a Bookmark Afterthought.

    Methods:
    str(self): Returns the afterthought id.
    """

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_afterthought")
    text = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.id

class BookmarkTag(MetaModel):
    """
    This model contains the data related to a Bookmark Tag.
    
    Methods:
    str(self): Returns the tag id.
    """

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_tag")
    tag = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.id

class BookmarkSource(MetaModel):
    """
    This model contains the data related to a Bookmark Source.

    Methods:
    str(self): Returns the source id.
    """
    base_url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.id

class BookMarkSourceMapping(MetaModel):
    """
    This model contains the data related to a Bookmark Source Mapping.

    Methods:
    str(self): Returns the source mapping id.
    """

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_source_mapping")
    source_mapping = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.id

class BookmarkList(MetaModel):
    """
    This model contains the data related to a Bookmark List.

    Methods:
    str(self): Returns the list id.
    """

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_list")
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id

class ExtraMetaFunctions(MetaModel):
    """
    This model contains the data related to a Bookmark Type.

    Methods:
    str(self): Returns the type id.
    """

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name="bookmark_type")
    is_referrence = models.BooleanField(default=False)
    is_later_read = models.BooleanField(default=False)
    reminder_time_for_later_read = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.id