from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
Paths to:
- Admin URL 'admin/' for the superuser.
- Cart URL 'cart/' to add items to the (Shopping) Cart.
- Payment URL 'payment/' to finalise payment using the Braintree Payment
System.
- Orders URL 'orders/' to create and submit orders to the payment system.
- Account URL 'account/' to handle user authentication and authorisation.
- Home URL '' for the Home / Landing Page of the project/website.
- Shop URL 'shop/' to view and add the items to order/purchase (courses and
coaching).
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('account/', include('account.urls')),
    path('', include('home.urls')),
    path('shop/', include('shop.urls', namespace='shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
