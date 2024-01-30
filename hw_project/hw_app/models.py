# Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.
# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента

# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара

# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа

from django.db import models
import datetime


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.name} {self.email}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
    adding_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'{self.product_name} price: {self.price}'

    def get_orders(self, customer_id):
        return list(Order.objects.filter(products__pk=self.pk, customer__pk=customer_id))


class Order(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def get_products(self):
        order_products = self.products.all()
        return order_products

    def get_timedelta(self):
        delta = datetime.date.today() - self.date_order
        return delta.days

    def __str__(self):
        return f'Order id: {self.pk} {self.customer}, date: {self.date_order}, amount: {self.amount}'
