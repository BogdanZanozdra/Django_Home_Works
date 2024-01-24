import logging


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Customer, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index got response')
    return HttpResponse(f'<h2>Главная страница</h1><br><h2>Контент главной страницы</h2><br><p>Подвал</p>')


def about_me(request):
    logger.info('about me got response')
    return HttpResponse(f'<h2>Обо мне</h2><br><p>Информация обо мне</p>')


def get_customers(request):
    customers = Customer.objects.all()
    return render(request, 'hw_app/customers.html', {'customers': customers})


def get_customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('date_order')
    return render(request, 'hw_app/user_orders.html', {'orders': orders, 'customer': customer})


def get_customer_orders_for_period(request, customer_id, period_days):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('date_order')
    return render(request, 'hw_app/orders_for_period.html', {'orders': orders, 'customer': customer, 'days': period_days})


def customer_products(request, customer_id, period_days):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('date_order')
    products_dict = {}
    product_orders = []
    for order in orders:
        if order.get_timedelta() <= period_days:
            for product in order.get_products():
                if product not in products_dict:
                    products_dict[str(product)] = product.get_orders(customer_id)
    return render(request, 'hw_app/customer_products.html', {'orders': orders, 'customer': customer,
                                                             'days': period_days, 'products_dict': products_dict})


