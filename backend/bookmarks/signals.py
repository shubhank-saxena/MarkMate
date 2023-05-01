from django.db.models.signals import post_save
from django.dispatch import receiver
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup

from backend.bookmarks.models import Bookmark, BookmarkSource

@receiver(post_save, sender=Bookmark)
def get_create_source(sender, instance, created, **kwargs):
    """
    Create a BookmarkSource instance if it does not exist.

    Args:
        sender (Bookmark): The Bookmark model.
        instance (Bookmark): The Bookmark instance.
        created (bool): Whether the instance was created or not.
    """

    source_url = instance.url
    source_url = urlsplit(source_url)
    source_url = source_url.scheme+'://'+source_url.netloc

    instance, created = BookmarkSource.objects.get_or_create(
        base_url=source_url
    )
    if created:
        # Retrieve the HTML content of the website
        response = requests.get(source_url)
        html = response.content

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Get the title from the meta tags
        title = soup.find('meta', property='og:title')
        if title is not None:
            title = title['content']
        else:
            title_tag = soup.find('title')
            if title_tag is not None:
                title = title_tag.text.strip()
            else:
                title = None

        # Get the image URL from the meta tags
        image = soup.find('meta', property='og:image')
        if image is not None:
            image = image['content']
        else:
            # Fallback to finding the first image in the HTML
            image_tag = soup.find('img')
            if image_tag is not None:
                image = image_tag['src']
            else:
                image = None

        instance.name = title
        instance.logo = image
        instance.save()
