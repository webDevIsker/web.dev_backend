import uuid
from django.db import models


class ProductsGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='Наименование', max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родитель',
                               related_name='group')

    def __str__(self):
        return f'{self.title} - {self.parent}'



    class Meta:
        verbose_name = 'Группа номенклатуры'
        verbose_name_plural = 'Группы номенклатур'


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name='Наименование полное', max_length=250)
    group = models.ForeignKey(ProductsGroup, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Группа',
                              related_name='products')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'
