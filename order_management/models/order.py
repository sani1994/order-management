import uuid

from django.db import models

from customer.models import Customer


class Order(models.Model):
    order_identifier = models.CharField(max_length=255, default=uuid.uuid4)
    product = models.ManyToManyField('order_management.OrderedProduct')
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)
    total_amount = models.DecimalField(default=0.0,decimal_places=1,max_digits=7)

    class Meta:
        app_label = 'order_management'

