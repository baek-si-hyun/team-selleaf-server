from django.urls import path

from cart.views import CartView, CartDetailView

app_name = 'cart'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('detail/<int:cart_id>', CartDetailView.as_view(), name='detail'),

]
