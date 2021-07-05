"""Circles Model"""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Circle model

    A circle is a group of users it can be public or private 
    and it can make invitations to join users to them
    """

    name = models.CharField('circle name', max_length=255)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures/', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known a oficial community')

    is_public = models.BooleanField(
        default=False
    )

    is_limited = models.BooleanField(
        default=False
    )

    members_limit = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        """Return circle name"""
        return self.name

    # Extend Meta info of CrideModel Meta
    class Meta(CRideModel.Meta):
        """Meta class"""
        ordering = ['-rides_taken', '-rides_offered']
