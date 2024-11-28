from django.contrib import admin

from service.models import RefBook, RefBookVersion, RefBookElement

class RefBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'display_current_version', 'display_start_date')
    
    def display_current_version(self,obj):
        return ''
    
    def display_start_date(self,obj):
        return ''

admin.site.register(RefBook, RefBookAdmin)

class RefBookVersionAdmin(admin.ModelAdmin):
    list_display = ('display_code_refbook', 'display_name_refbook', 'version', 'start_date')
    
    def display_code_refbook(self,obj):
        return ''
    
    def display_name_refbook(self, obj):
        return ''

admin.site.register(RefBookVersion, RefBookVersionAdmin)
admin.site.register(RefBookElement)
