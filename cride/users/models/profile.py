"""Profile model"""

#Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Profile(CRideModel):
    """
    A profile hold a user's public data like biograpy,
    picture and stadistics
    """
    #When user is delete profile to
    user = models.OneToOneField('users.User',on_delete=models.CASCADE)

    #Save image is posible for Pillow (see in requiriments)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, 
        null=True
    )

    biography = models.TextField(max_length=500,blank=True, null=True)

    #Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered"
    )

    def __str__(self):
        """Return profile representation"""
        return str(self.user)
