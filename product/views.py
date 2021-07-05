from django.views.generic import ListView

from product.models import Products


class ProductListView(ListView):
    model = Products
    template_name = 'order.html'

