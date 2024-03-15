from django.urls import path
from cart.views import CartView, CartListAPI, CartAPI, CartCheckoutAPI

app_name = 'apply'

urlpatterns = [
    path('', CartView.as_view(), name='apply'),

]
