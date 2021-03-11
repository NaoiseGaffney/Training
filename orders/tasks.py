from django.core.mail import send_mail
from .models import Order


"""
Email notification upon completed order. Email settings configured in
'Training/settings.py'.
"""


def order_created(order_id):
    """
    Send e-mail notifications.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.\n' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@training.com',
                          [order.email])
    return mail_sent
