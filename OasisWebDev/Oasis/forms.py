from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class RetrieveForm(ModelForm):
    class Meta:
        model = Products
        fields = ['SKU']


class UpdateForm(ModelForm):
    class Meta:
        model = Products
        fields = ['SKU', 'QTY', 'price']
