from django.urls import path
from . import views


"""
Paths to:
- Default '' providing the list of available products (courses and coaching
sessions).
- Product View list based upon category (courses or coaching).
- Product Detail View to view the details of a selected product (course or
coaching session).
"""
app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
