from django.urls import path
from .views import index, about_me, get_customers, get_user_orders


urlpatterns = [
    path('', index, name='index'),
    path('about_me/', about_me, name='about_me'),
    path('customers/', get_customers, name='get_costomers'),
    path('user_orders/<int:user_id>/', get_user_orders, name='user_orders'),
]

