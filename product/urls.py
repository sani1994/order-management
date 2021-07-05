from django.conf.global_settings import STATIC_ROOT
from django.conf.urls.static import static
from django.urls import path

from product.views import ProductListView
from shop_management_settings.settings import DEBUG, STATIC_URL

app_name = 'product'

urlpatterns = [
    path('order-product', ProductListView.as_view(), name='order-product'),
]
if DEBUG:
    urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
