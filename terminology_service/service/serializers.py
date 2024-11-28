from rest_framework.serializers import ModelSerializer

from service.models import Catalog, CatalogElement, CatalogVersion

class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

class CatalogVersionSerializer(ModelSerializer):
    class Meta:
        model = CatalogVersion
        fields = '__all__'

class CatalogElementSerializer(ModelSerializer):
    class Meta:
        model = CatalogElement
        fields = '__all__'