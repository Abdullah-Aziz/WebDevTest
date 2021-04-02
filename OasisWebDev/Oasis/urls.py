from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add_product/', views.product_register, name="add_product"),
    path('retrieve_product/', views.product_retrieve, name="retrieve_product"),
    path('filter_product/', views.product_filter, name="filter_product"),
    # path('search_product/', views.product_search, name="search_product"),
    path('remaining_products/', views.product_remaining, name="list_available_products"),
    path('sold_products/', views.product_sold, name="list_sold_products"),
    path('update_product/', views.product_update, name="update_product"),
    ]
