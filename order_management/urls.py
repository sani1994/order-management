from django.conf.urls.static import static
from django.urls import path

from order_management.views import order_submit_view, order_pdf_view
from shop_management_settings import settings
from shop_management_settings.settings import DEBUG

app_name = 'order_management'

urlpatterns = [
    path('order-product/submit/', order_submit_view, name='order-submit'),
    path('order-product/submit/<int:id>', order_pdf_view, name='order-pdf'),
]
if DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
