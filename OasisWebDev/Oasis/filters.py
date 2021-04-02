from django.contrib.auth.models import User
import django_filters
from .models import Products


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ['SKU']