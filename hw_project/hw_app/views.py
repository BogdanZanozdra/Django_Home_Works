import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Customer, Product, Order
from .forms import UpdateOrderForm, ProductForm

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
    return render(request, 'hw_app/orders_for_period.html',
                  {'orders': orders, 'customer': customer, 'days': period_days})


def customer_products(request, customer_id, period_days):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('date_order')
    products_dict = {}
    for order in orders:
        if order.get_timedelta() <= period_days:
            for product in order.get_products():
                if product not in products_dict:
                    products_dict[str(product)] = product.get_orders(customer_id)
    return render(request, 'hw_app/customer_products.html', {'orders': orders, 'customer': customer,
                                                             'days': period_days, 'products_dict': products_dict})


def update_order(request, order_id):
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST)
        message: str = 'Заполнена не верно!'
        if form.is_valid():
            amount = form.cleaned_data['amount']
            date_order = form.cleaned_data['date_order']
            customer = form.cleaned_data['customer']
            products = form.cleaned_data['products']
            order = Order.objects.filter(pk=order_id).first()
            order.amount = amount
            order.date_order = date_order
            order.customer = customer
            order.products.set(products)
            print(products)
            print(order.products)
            order.save()
            message: str = 'Заказ отредактирован!'
            # logger.info(f'New values: {customer=}, {amount=}, {date_order=}')
    else:
        form = UpdateOrderForm()
        message: str = 'Заполните форму'
    return render(request, 'hw_app/update_order.html', {'form': form, 'message': message})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Создайте продукт'
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            adding_date = form.cleaned_data['adding_date']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(product_name=product_name, description=description, price=price, count=count,
                              adding_date=adding_date, image=image)
            product.save()
            message = 'Продукт сохранен'
    else:
        form = ProductForm()
        message = 'Создайте продукт'
    return render(request, 'hw_app/add_product.html', {'form': form, 'massage': message})


def get_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    return render(request, 'hw_app/product.html', {'product': product})
