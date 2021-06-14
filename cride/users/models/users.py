"""User models"""

# Django
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
    User model

    Extend from Django's Abstract User,change the username field to
    email field to do authentication and add some extra fields
    """

    """Email unique"""
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists.'
        }
    )

    """Phone number with max and nullable and correct format"""
    phone_regex = RegexValidator(
        regex=r'+?1?\d{9,15}$',
        message="Phone number must be entered with correct format"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True)

    """This user is client by default""" 
    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily to distinguish users of clients.'
            'Clients are the main type of users'
        )
    )

    """Account is verified"""
    is_verified = models.BooleanField(
        'account verified',
        default=False,
        help_text=(
            'Set True when user verify his email'
        )
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    """Field to do autehtication"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
