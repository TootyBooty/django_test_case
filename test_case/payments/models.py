from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=2000)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('payments:item_detail', args=[self.pk])