from django.urls import path
from . import views

"""
Paths to the:
- Create the Order using URL 'create/'.
- View the order detail in the Admin View using URL 'admin/order/<int:order_id>/'.
"""
app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path(
        'admin/order/<int:order_id>/',
        views.admin_order_detail,
        name='admin_order_detail'),
]
