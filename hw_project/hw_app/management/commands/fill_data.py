import random

from django.core.management.base import BaseCommand
from random import randint
from hw_app.models import Customer, Order, Product


class Command(BaseCommand):
    help = 'Filling database'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count for filling data')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        product_list = []
        for i in range(1, count**3 + 1):
            product = Product(
                product_name=f'Product {i}',
                description='Lorem ipsum',
                price=float(f'{i}.99'),
                count=10
            )
            product_list.append(product)
            product.save()
            self.stdout.write(f'{product}')

        for i in range(1, count + 1):
            customer = Customer(
                name=f'Name {i}',
                email=f'{i}@mail.com',
                phone_number=f'8{i}, {i}, {i}',
                address=f'Street{i}'
            )
            self.stdout.write(f'{customer}')
            customer.save()
            for j in range(count + 1):
                order = Order(
                    customer=customer,
                    amount=0
                )
                order.save()
                order.products.set([random.choice(product_list) for _ in range(1, count + 1)])
                amount_for_set = sum([order_product.price for order_product in order.products.all()])
                order.amount = amount_for_set
                order.save()

                self.stdout.write(f'{order}')
                self.stdout.write(f'Order products: {order.products.all()}\nOrder total amount: {order.amount}')

