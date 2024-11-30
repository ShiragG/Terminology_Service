from rest_framework.serializers import ModelSerializer

from service.models import RefBook, RefBookVersion, RefBookElement

class RefBookSerializer(ModelSerializer):
    class Meta:
        model = RefBook
        fields = ['id', 'code', 'name']

class RefBookVersionSerializer(ModelSerializer):
    class Meta:
        model = RefBookVersion
        fields = '__all__'

class RefBookElementSerializer(ModelSerializer):
    class Meta:
        model = RefBookElement
        fields = '__all__'