"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#Serializers
from cride.users.serializers import UserLoginSerializer,UserModelSerializer


class UserLoginAPIView(APIView):
    """User login API View"""

    def post(self,request,*arg,**kwargs):
        """Handle HTTP POST request"""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validation(data=request.data)
        user, token = serializer.save()

        data = {
            'user':UserModelSerializer(user).data,
            'token':token
        }

        return Response(data,status=status.HTTP_201_CREATED)
