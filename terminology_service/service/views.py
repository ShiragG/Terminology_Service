from rest_framework.viewsets import ModelViewSet

from service.models import Catalog, CatalogElement, CatalogVersion
from service.serializers import CatalogSerializer, CatalogElementSerializer, CatalogVersionSerializer


class CatalogViewSet(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class CatalogElementViewSet(ModelViewSet):
    queryset = CatalogElement.objects.all()
    serializer_class = CatalogElementSerializer

class CatalogVersionViewSet(ModelViewSet):
    queryset = CatalogVersion.objects.all()
    serializer_class = CatalogVersionSerializer
