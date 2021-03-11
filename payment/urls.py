from django.urls import path
from . import views


"""
Paths to the:
- Processing the payment using the Braintree Payment System.
- Done upon successful payment.
- Canceled upon an error in the payment.
"""
app_name = 'payment'
urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
