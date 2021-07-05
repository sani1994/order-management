from django.contrib import admin

# Register your models here.
from product.models import *

admin.site.register(Products)
admin.site.register(Category)
