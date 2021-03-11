from .cart import Cart


"""
Context processor for the (Shopping )Cart to make it available across the project/website.
Upper right-hand corner on Desktop/Tablet screens has the (Shopping) Cart.
Last item in the hamburger-menu-sidenav for Mobile screens has the (Shopping) Cart.
"""


def cart(request):
    return {'cart': Cart(request)}
