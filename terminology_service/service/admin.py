from django.contrib import admin
from django.utils import timezone

from service.models import RefBook, RefBookVersion, RefBookElement

class RefBookVersionInline(admin.TabularInline):
    model = RefBookVersion
    extra = 1
    verbose_name = 'Версия справочника'
    verbose_name_plural = 'Версии справочника'


@admin.register(RefBook)
class RefBookAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'code', 'name', 'get_current_version', 'get_current_start_date')
    inlines = [RefBookVersionInline]
    current_date = timezone.now().date()
    
    def get_id(self,obj):
        return obj.id
    get_id.short_description = 'Идентификатор'
    
    def get_current_version(self,obj):
        return obj.refbookversion_set.filter(start_date__lte=self.current_date).order_by('-start_date').first().version
    get_current_version.short_description = 'Текущая версия'
    
    def get_current_start_date(self,obj):
        return obj.refbookversion_set.filter(start_date__lte=self.current_date).order_by('-start_date').first().start_date
    get_current_start_date.short_description = 'Дата начала версии'


class RefBookElementInline(admin.TabularInline):
    model = RefBookElement
    extra = 1
    verbose_name = 'Элемент справочника'
    verbose_name_plural = 'Элементы справочника'

@admin.register(RefBookVersion)
class RefBookVersionAdmin(admin.ModelAdmin):
    list_display = ('get_code_refbook', 'get_name_refbook', 'version', 'start_date')
    inlines = [RefBookElementInline]
    
    def get_code_refbook(self,obj):
        return obj.refbook_id.code
    get_code_refbook.short_description = 'Код справочника'
    
    def get_name_refbook(self, obj):
        return obj.refbook_id.name
    get_name_refbook.short_description = 'Наименование справочника'

admin.site.register(RefBookElement)
