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


def get_user_orders(request, user_id):
    user = get_object_or_404(Customer, pk=user_id)
    orders = Order.objects.filter(customer=user)
    return render(request, 'hw_app/user_orders.html', {'orders': orders, 'user': user})
