from django.contrib import admin

from .models import Catalog, CatalogVersion, CatalogElement

# Register your models here.

admin.site.register([Catalog,CatalogVersion,CatalogElement])