"""Circles Serializers"""


#Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from cride.circles.models import Circle

class CircleSerializer(serializers.Serializer):
    """Circle Serializer"""

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):
    """Create Circle Serializer"""
    name = serializers.CharField(
        max_length=140,
        required=True,
        validators = [
            UniqueValidator(queryset=Circle.objects.all())
        ]
    )
    slug_name = serializers.CharField(
        max_length=140,
        required=True,
        validators = [
            UniqueValidator(queryset=Circle.objects.all())
        ]
    )
    about = serializers.CharField(
        max_length=255,
        required=False
    )

    def create(self,data):
        return Circle.objects.create(**data)
