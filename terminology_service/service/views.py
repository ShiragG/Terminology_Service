from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from service.models import RefBook, RefBookElement, RefBookVersion
from service.serializers import RefBookSerializer, RefBookVersionSerializer


class RefBookListView(ListAPIView):
    serializer_class = RefBookSerializer
    
    def get_queryset(self):
        date_param = self.request.query_params.get('date', None)
        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
                return RefBook.objects.filter(refbookversion__start_date__lte=date).distinct()
            except:
                return None
        print('all')
        return RefBook.objects.all()
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({"refbooks": serializer.data}) 

class RefBookElementListView(ListAPIView):
    serializer_class = RefBookVersionSerializer
    
    def get_queryset(self):
        return ''

