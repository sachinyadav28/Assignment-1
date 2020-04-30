from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from user.jwt.permissions import AnonPermissionOnly

from status.serializers import StatusInlineUserSerializer
from status.views import StatusAPIView
from status.models import Status

from .serializers import UserDetailSerializer

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    #permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    queryset            = User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username' # id

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(StatusAPIView):
    serializer_class            = StatusInlineUserSerializer
    
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)

