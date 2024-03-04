from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart, CartDetail
from member.models import Member


# 장바구니 서비스
class CartView(View):
    # 장바구니 페이지로 이동
    def get(self,request):
        # member = request.session['member']
        # print(member)
        return render(request,'cart/cart.html')

    def post(self,request):
        # 로그인 정보로 멤버 불러오기
        member = Member(**request.session['member'])
        print(member)

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


class CartUpdateView(View):
    # lecture detail 페이지에서 버튼을 누르면 정보입력
    # lecture detail urls 에서 작업을 해야하는 부분인가?

    def post(self,request,lecture_id):
        data = request.POST
        member = request.session['member']
        data = {
            'quantity': data['counted-number'],
            'cart_id': Cart.objects.filter(member=member).first(),
            # 이 부분 url에 어떻게 지정되는 지 확인
            'lecture_id': lecture_id,
            'date': data['date'],
            'time': data['time'],
            'kit': data['kit'],

        }


        # 동일 품목이 있는지 검사 해야하는 부분
        # 있다면 quantity에 +1
        # 없다면 CartDetail에 create
        cart_detail = CartDetail.objects.create(**data)

        return redirect('cart/detauk')

class CartDetailView(View):
    pass