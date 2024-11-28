from rest_framework.viewsets import ModelViewSet

from service.models import RefBook, RefBookElement, RefBookVersion
from service.serializers import RefBookSerializer, RefBookElementSerializer, RefBookVersionSerializer


class RefBookViewSet(ModelViewSet):
    queryset = RefBook.objects.all()
    serializer_class = RefBookSerializer

class RefBookElementViewSet(ModelViewSet):
    queryset = RefBookElement.objects.all()
    serializer_class = RefBookElementSerializer

class RefBookVersionViewSet(ModelViewSet):
    queryset = RefBookVersion.objects.all()
    serializer_class = RefBookVersionSerializer
