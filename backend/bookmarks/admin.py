from django.contrib import admin
from backend.bookmarks.models import Bookmark, BookmarkTag, BookmarkSource, BookmarkList

admin.site.register(Bookmark)
admin.site.register(BookmarkTag)
admin.site.register(BookmarkSource)
admin.site.register(BookmarkList)