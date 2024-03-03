import requests
from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart, CartDetail
from member.models import Member


# 장바구니 서비스
class CartView(View):
    # 장바구니 페이지로 이동
    def get(self,request):
        return render(request,'cart/cart.html')

    def post(self,request):
        # 로그인 정보로 멤버 불러오기
        member = Member(**request.session['member'])
        # 장바구니 불러오기
        my_cart = Cart.objects.filter(status=0, member=member)
        # 장바구니 검사
        # 기존 장바구니가 존재하지 않으면
        if not my_cart.exists():
            # 새로운 장바구니 생성
            my_cart = Cart.objects.create(member = member)
        # 기존 장바구니가 존재하면
        else:
            # 장바구니를 불러온다.
            my_cart = my_cart.first()

        return redirect(my_cart.get_absolute_url())


class CartDetailView(View):

    def post(self,request):
        data = request.post
        member = request.session['member']
        data = {
            'quantity':data['counted-number'],
            'cart_id': Cart.objects.filter(member=member).first(),
            # 강의 정보를 어떻게 가져올지는 더미데이터 필요
            'lecture_id':data['lecture-id']

        }

        CartDetail.objects.create(**data)

        return redirect('cart:cart')