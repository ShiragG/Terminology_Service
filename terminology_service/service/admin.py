from django.contrib import admin

from .models import Catalog, CatalogVersion, CatalogElement

admin.site.register([Catalog,CatalogVersion,CatalogElement])