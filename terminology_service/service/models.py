from django.db import models


class Catalog(models.Model):
    code = models.CharField(max_length=100, blank=False, null=False, unique=True,help_text='')
    name = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField()

class CatalogVersion(models.Model):
    catalog_id = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=False, null=False)
    version = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField()

class CatalogElement(models.Model):
    catalog_version_id = models.ForeignKey(CatalogVersion, on_delete=models.CASCADE, blank=False, null=False)
    code = models.CharField(max_length=100, blank=False, null=False)
    value = models.CharField(max_length=300, blank=False, null=False)