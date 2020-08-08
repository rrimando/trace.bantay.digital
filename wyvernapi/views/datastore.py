from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny

from wyvernuser.permissions import (
    IsAdminUser,
    IsOwner,
    IsEditorUser,
    IsModeratorUser,
    IsAdminOrModeratorUser,
    IsMemberUser,
    IsOwner,
    IsLoggedInUserOrAdmin,
    IsAdminOrAnonymousUser,
)
from wyverndatastorage.models import WyvernDataStore
from wyvernapi.serializers.datastore import (
    WyvernDataStoreSerializer,
    WyvernDataStoredSerializer,
)


class WyvernDataStoreViewSet(ModelViewSet):
    queryset = WyvernDataStore.objects.all()
    serializer_class = WyvernDataStoreSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        data_filter = self.request.GET.get("data_filter")
        data_limit = self.request.GET.get("data_limit")

        data = WyvernDataStore.objects.filter(data_store_identity=data_filter)

        if data_limit:
            data = data.order_by("-id")[: int(data_limit)]

        return data

    def get_permissions(self):
        permission_classes = []
        if self.action == "create":
            authentication_classes = []
            permission_classes = []
        elif self.action == "list":
            self.serializer_class = WyvernDataStoredSerializer
            authentication_classes = []  # Have to add Token back in the future
            permission_classes = []
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == "destroy":
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]
