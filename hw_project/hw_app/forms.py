import datetime
from django import forms

from .models import Customer, Product


class UpdateOrderForm(forms.Form):
    amount = forms.DecimalField(max_digits=5, decimal_places=2)
    date_order = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'class': 'form-control',
                                                               'type': 'date'}))
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    count = forms.IntegerField(min_value=0)
    adding_date = forms.DateField(initial=datetime.date.today,
                                  widget=forms.DateInput(attrs={'class': 'form-control',
                                                                'type': 'date'}))
    image = forms.ImageField()

