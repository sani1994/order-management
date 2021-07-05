import decimal

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from order_management.models import OrderedProduct
from order_management.models.order import Order
from product.models import Products
from customer.models import Customer


def order_submit_view(request):
    order_obj = Order()
    total = 0
    ordered_products = []
    order_product = OrderedProduct()
    data = request.POST
    data = dict(data.lists())  # convert querydict to normal dict
    data.pop('csrfmiddlewaretoken')
    user = Customer(
        name=data.pop('customer_name'),
        phone_number=data.pop('phone_number'),
        email=data.pop('email')
    )
    user.save()
    order_obj.user_id = user.id
    for _k, _v in data.items():
        product = Products.objects.filter(code=_k).last()
        if product:
            order_product.product_id = product.id
            order_product.qty = int(_v[0])
            order_product.save()
            ordered_products.append(order_product)
            total += product.unit_price * decimal.Decimal(_v[0])
    order_obj.total_amount = total
    order_obj.save()
    order_obj.product.add(*ordered_products)
    return JsonResponse({
        'order_id': order_obj.id
    })


def order_pdf_view(request, id):
    order_obj = Order.objects.filter(id=id).last()
    return render(request, 'order_pdf.html', {'obj': order_obj})
