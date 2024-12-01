from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from service.models import RefBook, RefBookElement, RefBookVersion
from service.serializers import RefBookSerializer, RefBookElementSerializer


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
    serializer_class = RefBookElementSerializer

    def get_queryset(self):
        refbook_id = self.kwargs['id']
        refbook = get_object_or_404(RefBook, id=refbook_id)

        version_param = self.request.query_params.get('version', None)

        

        if version_param:
            refbook_version = get_object_or_404(
                RefBookVersion, refbook_id=refbook, version=version_param)
        else:
            current_date = timezone.now().date()
            refbook_version = RefBookVersion.objects.filter(
                refbook_id=refbook,
                start_date__lte=current_date
            ).order_by('-start_date').first()

            if not refbook_version:
                return RefBookElement.objects.none()

        return RefBookElement.objects.filter(refbook_version_id=refbook_version)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({"elements": serializer.data})

class RefBookCheckElementView(ListAPIView):
    serializer_class = RefBookElementSerializer
    
    def get_queryset(self):
        refbook_id = self.kwargs['id']
        refbook = get_object_or_404(RefBook, id=refbook_id)
    
        code = self.request.query_params.get('code', None)
        value = self.request.query_params.get('value', None)
        
        if not code or not value:
            return RefBookElement.objects.none()
        
        version_param = self.request.query_params.get('version', None)
        if version_param:
            refbook_version = RefBookVersion.objects.filter(refbook_id=refbook, version=version_param).first()
            if not refbook_version:
                return RefBookElement.objects.none()
        else:
            current_date = timezone.now().date()
            refbook_version = RefBookVersion.objects.filter(
                refbook_id=refbook,
                start_date__lte=current_date
            ).order_by('-start_date').first()

            if not refbook_version:
                return RefBookElement.objects.none()

        print(refbook_version)
        return RefBookElement.objects.filter(refbook_version_id=refbook_version, code=code, value=value)
        
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({"element": serializer.data})
