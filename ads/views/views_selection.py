from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import  Selection
from ads.permissions.permissions import IsOwner, IsModerator

from ads.serializers.selection_serialize import SelectionSerializer, SelectionListSerializer, SelectionCreateSerializer, \
    SelectionDetailSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.order_by('name')
    default_serializer_class = SelectionSerializer

    default_permission = [AllowAny]

    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwner | IsModerator],
        "partial_update": [IsAuthenticated, IsOwner | IsModerator],
        "destroy": [IsAuthenticated, IsOwner | IsModerator]
    }

    serializers = {
        "list": SelectionListSerializer,
        "create": SelectionCreateSerializer,
        "retrieve": SelectionDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


