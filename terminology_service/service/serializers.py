from rest_framework.serializers import ModelSerializer

from service.models import RefBook, RefBookVersion, RefBookElement

class RefBookSerializer(ModelSerializer):
    class Meta:
        model = RefBook
        fields = ['id', 'code', 'name']

class RefBookElementSerializer(ModelSerializer):
    class Meta:
        model = RefBookElement
        fields = ['code', 'value']