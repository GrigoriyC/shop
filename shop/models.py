from django.db import models

class Product(models.Model):
  title = models.CharField(max_length=200, verbose_name="Наименование")
  text = models.TextField(verbose_name="Описание")
  price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'товар'
    verbose_name_plural = 'товары'
    db_table = 'shop_products'

  def __str__(self):
    return self.title
