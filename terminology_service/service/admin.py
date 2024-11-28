from django.contrib import admin

from service.models import Catalog, CatalogVersion, CatalogElement

# admin.site.register([Catalog,CatalogVersion,CatalogElement])

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'display_current_version', 'display_start_date')
    
    def display_current_version(self,obj):
        return ''
    
    def display_start_date(self,obj):
        return ''

admin.site.register(Catalog, CatalogAdmin)

class CatalogVersionAdmin(admin.ModelAdmin):
    list_display = ('display_code_catalog', 'display_name_catalog', 'version', 'start_date')
    
    def display_code_catalog(self,obj):
        return ''
    
    def display_name_catalog(self, obj):
        return ''

admin.site.register(CatalogVersion, CatalogVersionAdmin)
admin.site.register(CatalogElement)
