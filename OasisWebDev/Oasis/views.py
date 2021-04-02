from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm, RetrieveForm, UpdateForm
# Create your views here.

from .filters import UserFilter


def product_filter(request):
    user_list = Products.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    product = user_filter
    return render(request, 'Oasis/product_filter.html', {'product': product})


def home(request):
    return render(request, 'Oasis/home.html', {})


def product_register(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'Oasis/product_add.html', context)


def product_retrieve(request):

    search_sku = request.POST.get('name')
    products = Products.objects.all()
    retrieved_product = None
    for product in products:
        if product.SKU == search_sku:
            retrieved_product = product

    return render(request, 'Oasis/product_detail.html', {'product': retrieved_product})


def product_update(request):
    products = Products.objects.all()
    product = UserFilter(request.GET, queryset=products)
    # if product.qs:
    #     form = UpdateForm(request.POST, instance=product.qs[0])
    # else:
    #     form = UpdateForm()
    # if form.is_valid():
    #     form.save()

    form = UpdateForm(instance=product.qs.first())

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=product.qs.first())
        if form.is_valid():
            form.save()

    context = {'form': form,
               'product': product}
    return render(request, 'Oasis/product_update.html', context)


def product_remaining(request):
    products = Products.objects.all()
    remaining = []

    for product in products:
        if product.QTY > 0:
            print(type(product))
            # What to show?
            remaining.append(product)

    return render(request, 'Oasis/ProductsRemainSold.html', {'products': remaining})


def product_sold(request):
    products = Products.objects.all()
    sold = []

    for product in products:
        if product.QTY == 0:
            # What to show?
            sold.append(product)

    return render(request, 'Oasis/ProductsRemainSold.html', {'products': sold})
#
#
# def customer(request, pk_test):
#     customer = Customer.objects.get(id=pk_test)
#
#     orders = customer.order_set.all()
#     order_count = orders.count()
#
#     myFilter = OrderFilter(request.GET, queryset=orders)
#     orders = myFilter.qs
#
#     context = {'customer': customer, 'orders': orders, 'order_count': order_count,
#                'myFilter': myFilter}
#     return render(request, 'accounts/customer.html', context)
#
# def updateOrder(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#     context = {'form': form}
#     return render(request, 'accounts/order_form.html', context)