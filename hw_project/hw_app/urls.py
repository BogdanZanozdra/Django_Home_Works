from django.urls import path
from .views import index, about_me, get_customers, get_customer_orders, get_customer_orders_for_period, \
    customer_products

urlpatterns = [
    path('', index, name='index'),
    path('about_me/', about_me, name='about_me'),
    path('customers/', get_customers, name='get_customers'),
    path('customer_orders/<int:customer_id>/', get_customer_orders, name='customer_orders'),
    path('customer_orders_for_period/<int:customer_id>/<int:period_days>/', get_customer_orders_for_period,
         name='customer_orders_for_period'),
    path('customer_products/<int:customer_id>/<int:period_days>/', customer_products, name='customer_products'),

]
