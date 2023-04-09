import uuid

from django.db import models


class MetaModel(models.Model):
    """
    This model contains the meta data of a model.

    Note: This is an abstract model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta properties of the model."""

        abstract = True


class MetaModelWithUUID(models.Model):
    """
    This model contains the meta data of a model with UUID.

    Note: This is an abstract model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta properties of the model."""

        abstract = True