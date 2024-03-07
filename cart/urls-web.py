from django.urls import path
from cart.views import CartView, CartListAPI, CartAPI

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('list/<int:cart_id>/', CartListAPI.as_view()),
    path('<int:detail_id>/',CartAPI.as_view())
]
