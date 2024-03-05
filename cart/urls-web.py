from django.urls import path

from cart.views import CartView, CartDetailView

app_name = 'cart'

urlpatterns = [
    path('cart/<int:cart_id>', CartView.as_view(), name='cart'),
]
