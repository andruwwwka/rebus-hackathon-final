from rest_framework import viewsets

from registry.models import Registry
from registry.serializers import RegistrySerializer


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
