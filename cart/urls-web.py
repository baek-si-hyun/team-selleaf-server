from django.urls import path
from cart.views import CartView, CartUpdateView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('update/<int:lecture_id>/', CartUpdateView.as_view(), name='update_cart'),
]