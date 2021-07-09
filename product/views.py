from django.shortcuts import render
from django.views.generic import ListView

from customer.forms import CustomerForm
from product.models import Products


class ProductListView(ListView):
    model = Products
    template_name = 'order.html'


def product_list_view(request):
    customer_form = CustomerForm()
    return render(request, 'order.html', {'customer_form': customer_form})
