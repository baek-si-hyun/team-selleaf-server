from django.shortcuts import render
from django.views import View

# 장바구니 서비스
class CartView(View):
    # 장바구니 페이지로 이동
    def get(self,request):
        return render(request,'cart/cart.html')

    def post(self):
        pass

