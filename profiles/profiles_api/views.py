from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from profiles_api.models import UserProfile
from profiles_api.serializers import HelloApiSerializer, UserProfileSerializer


class HelloApiView(APIView):
    def get(self, request, format=None):
        return Response({'hello': 'world'})

    def post(self, request, format=None):
        serializer = HelloApiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'hello': serializer.data['name']})

    def delete(self, request, format=None):
        return Response({'method': 'delete'})


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    model = UserProfile
    queryset = UserProfile.objects.all()
    filterset_fields = ['username', 'is_active']

