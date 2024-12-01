from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from service.models import RefBook, RefBookElement, RefBookVersion
from service.serializers import RefBookSerializer, RefBookElementSerializer


class RefBookListView(ListAPIView):
    serializer_class = RefBookSerializer

    def get_queryset(self):
        date_param = self.request.query_params.get('date', None)
        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
                refbooks = RefBook.objects.filter(refbookversion__start_date__lte=date).distinct()
            except ValueError:
                refbooks = RefBook.objects.none()
        else:
            refbooks = RefBook.objects.all()

        return refbooks
    
    @swagger_auto_schema( manual_parameters=[
            openapi.Parameter('date', openapi.IN_QUERY, description="Дата в формате YYYY-MM-DD", type=openapi.TYPE_STRING, required=False,default=None),
        ])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
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

        return RefBookElement.objects.filter(refbook_version=refbook_version)

    @swagger_auto_schema( manual_parameters=[
            openapi.Parameter('version', openapi.IN_QUERY, description="Версия справочника", type=openapi.TYPE_STRING, required=False, default=None),
        ])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
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
            refbook_version = RefBookVersion.objects.filter(
                refbook_id=refbook, version=version_param).first()
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

        return RefBookElement.objects.filter(refbook_version=refbook_version, code=code, value=value)

    @swagger_auto_schema( manual_parameters=[
            openapi.Parameter('code', openapi.IN_QUERY, description="Код элемента справочника", type=openapi.TYPE_STRING, required=True, default=None),
            openapi.Parameter('value', openapi.IN_QUERY, description="Значение элемента справочника", type=openapi.TYPE_STRING, required=True, default=None),
            openapi.Parameter('version', openapi.IN_QUERY, description="Версия справочника", type=openapi.TYPE_STRING, required=False, default=None),
        ])
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({"element": serializer.data})

