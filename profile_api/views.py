from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profile_api import serializers
from profile_api import models
from profile_api import permissions


class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIViews features"""
        an_apiview = [
            'uses HTTP methods as functions(get, post, patch, put, delete)',
            'is similar to traditional Django View',
            'is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})


    def post(self, request):
        """create  a helllo message With our Name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )


    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """partials update of an Object"""

        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """to delete an object"""

        return Response({'method':'Delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API for viewsets"""

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update and partial update'
            'automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handling creating and Updating Models"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )

