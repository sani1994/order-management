from django.db import models

from product.models import Products


class OrderedProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(default=0)
    total = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.qty} - {self.total}"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.total = self.product.unit_price * self.qty
        super(OrderedProduct, self).save(force_insert=False, force_update=False, using=None,
                                         update_fields=None)

    class Meta:
        app_label = 'order_management'
