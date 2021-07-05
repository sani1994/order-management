from django.contrib import admin

# Register your models here.
from order_management.models.order import Order

admin.site.register(Order)
