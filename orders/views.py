from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm
from account.forms import UserEditForm, ProfileEditForm


"""
Order methods for:
- Create order. Three forms are created for authenticated and anonymous users.
 Two are populated for authenticated users when placing an order.
- View order details in the Admin View.
"""


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm()
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
        else:
            form = OrderCreateForm()
            user_form = UserEditForm()
            profile_form = ProfileEditForm()
    return render(request, 'order/create.html', {'cart': cart, 'user_form': user_form, 'profile_form': profile_form, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})
