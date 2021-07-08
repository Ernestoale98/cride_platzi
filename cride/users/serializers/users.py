"""Users serializers"""

#Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator


#Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#Models
from cride.users.models import User,Profile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )




class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer"""

    """Emal and user name validations"""
    email = serializers.EmailField(
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username= serializers.CharField(
        min_length=3,
        max_length=20,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    """Phone number validations"""
    phone_regex = RegexValidator(
        # regex=r'(+?1?\d{9,15}$)',
        message="Phone number must be entered with correct format"
    )
    phone_number = serializers.CharField(
        validators=[phone_regex]
    )

    """Password validations"""
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    """Name Validations"""
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)


    def validate(self,data):
        """Check password and password_confirmatio are equals"""
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords doesn't match")
        password_validation.validate_password(data['password'])
        return data



    def create(self,data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)
        return user









class UserLoginSerializer(serializers.Serializer):
    """User login serializer"""

    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self,data):
        """Check Credentials"""

        user = authenticate(
            username=data['email'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data


    def create(self,data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
