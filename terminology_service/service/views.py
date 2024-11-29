from rest_framework.views import APIView

from service.models import RefBook, RefBookElement, RefBookVersion
from service.serializers import RefBookSerializer, RefBookElementSerializer, RefBookVersionSerializer


# class RefBookViewSet(APIView):
    
#     def get(self, request):
#         return 'lift'
#     # queryset = RefBook.objects.all()
#     # serializer_class = RefBookSerializer

# class RefBookElementViewSet(APIView):
#     # queryset = RefBookElement.objects.all()
#     # serializer_class = RefBookElementSerializer
#     pass

# class RefBookVersionViewSet(APIView):
#     # queryset = RefBookVersion.objects.all()
#     # serializer_class = RefBookVersionSerializer
#     pass
