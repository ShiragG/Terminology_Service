from rest_framework.serializers import ModelSerializer

from service.models import RefBook, RefBookVersion, RefBookElement

class RefBookSerializer(ModelSerializer):
    class Meta:
        model = RefBook
        fields = ['id', 'code', 'name']
        extra_kwargs = {
            'code':{'help_text':'Код справочника'},
            'name':{'help_text':'Наименование справочника'},
        }

class RefBookElementSerializer(ModelSerializer):
    class Meta:
        model = RefBookElement
        fields = ['code', 'value']
        extra_kwargs = {
            'code':{'help_text':'Код элемента'},
            'value':{'help_text':'Значение элемента'},
        }

class RefBookRefBookVersionSerializer(ModelSerializer):
    class Meta:
        model = RefBookVersion
        fields = '__all__'