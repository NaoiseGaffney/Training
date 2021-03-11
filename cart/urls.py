from django.urls import path
from . import views


"""
Paths to the:
- default cart ''
- adding an item to the cart
- removing an item (number of items per product) from the cart
"""
app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
