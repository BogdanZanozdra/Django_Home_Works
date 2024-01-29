from django.urls import path
from .views import index, about_me, get_customers, get_customer_orders, get_customer_orders_for_period, \
    customer_products, update_order, add_product, get_product

urlpatterns = [
    path('', index, name='index'),
    path('about_me/', about_me, name='about_me'),
    path('customers/', get_customers, name='get_customers'),
    path('customer_orders/<int:customer_id>/', get_customer_orders, name='customer_orders'),
    path('customer_orders_for_period/<int:customer_id>/<int:period_days>/', get_customer_orders_for_period,
         name='customer_orders_for_period'),
    path('customer_products/<int:customer_id>/<int:period_days>/', customer_products, name='customer_products'),
    path('update_order/<int:order_id>/', update_order, name='update_order'),
    path('add_product', add_product, name='add_product'),
    path('product/<int:product_id>/', get_product, name='get_product'),
]
