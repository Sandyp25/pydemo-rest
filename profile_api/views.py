from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Return a list of APIViews features"""
        an_apiview = [
            'uses HTTP methods as functions(get, post, patch, put, delete)',
            'is similar to traditional Django View',
            'is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

