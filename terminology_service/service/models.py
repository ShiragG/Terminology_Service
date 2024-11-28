from django.db import models


class RefBook(models.Model):

    code = models.CharField(max_length=100, blank=False,
                            null=False, unique=True, help_text='', verbose_name='Код')
    name = models.CharField(max_length=300, blank=False,
                            null=False, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return self.code


class RefBookVersion(models.Model):

    refbook_id = models.ForeignKey(
        RefBook, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Идентификатор справочника')
    version = models.CharField(
        max_length=50, blank=False, null=False, verbose_name='Версия')
    start_date = models.DateField(
        verbose_name='Дата начала действия версии', blank=True, null=True)

    class Meta:
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочника'

        unique_together = (['refbook_id', 'version'], [
                           'refbook_id', 'start_date'])

    def __str__(self):
        return self.version


class RefBookElement(models.Model):

    refbook_version_id = models.ForeignKey(
        RefBookVersion, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Идентификатор версии справочника')
    code = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name='Код элемента')
    value = models.CharField(max_length=300, blank=False,
                             null=False, verbose_name='Значение элемента')

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'

        unique_together = (['refbook_version_id', 'code'])

    def __str__(self):
        return self.code
