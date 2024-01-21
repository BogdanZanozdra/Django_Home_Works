from django.core.management.base import BaseCommand
from hw_app.models import Customer, Order


class Command(BaseCommand):
    help = 'delete order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user_id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'ID: {order.id} {order}')
        if order is not None:
            order.delete()




