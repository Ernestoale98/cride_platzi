"""Django models utilities"""

# Django
from django.db import models

"""CRideModel acts as abstract class"""
"""
This class add created_at and updated_at fields to the children models
created_at is a DateTime to store datetime of the object was created
updated_at is a DateTime to store last datetime when de object was modified
"""


class CRideModel(models.Model):
    created_at = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Datetime of when the object was created'
    )
    updated_at = models.DateTimeField(
        'updated_at',
        auto_now=True,
        help_text='Datetime of when the object was updated'
    )

    """Meta Options"""

    class Meta:
        abstract = True,
        # Latest by ascending created_at.
        get_latest_by = "created_at",
        # The default ordering for the object, for use when obtaining lists of objects
        # ASC -DESC
        ordering = ['-created_at', '-updated_at']
