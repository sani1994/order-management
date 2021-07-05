from django.db import models


class Products(models.Model):
    code = models.CharField(max_length=50, default=None, null=True, blank=True)
    name = models.CharField(max_length=255, default=None)
    unit_price = models.DecimalField(default=0, decimal_places=1, max_digits=7)
    category = models.ForeignKey('product.Category', on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = 'product'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Products, self).save(force_insert=False, force_update=False, using=None,
                                   update_fields=None)

    def __str__(self):
        return f"{self.code}-{self.name}"
