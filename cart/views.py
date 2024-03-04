from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart, CartDetail
from member.models import Member


# 장바구니 서비스
class CartView(View):
    # 장바구니 페이지로 이동
    def get(self, request):
        member = request.session.get('member')  # 세션에서 멤버 정보 가져오기
        if member:
            # 멤버 정보가 있는 경우
            my_cart = Cart.objects.filter(member=member, cart_status=0).first()
            if not my_cart:
                # 장바구니가 없는 경우 새로운 장바구니 생성
                my_cart = Cart.objects.create(member=member)
        else:
            # 멤버 정보가 없는 경우 로그인 페이지로 이동
            return redirect('login')  # 로그인 페이지의 URL로 수정 필요

        return render(request, 'cart/cart.html', {'cart': my_cart})



class CartUpdateView(View):
    # lecture detail 페이지에서 버튼을 누르면 정보입력
    # lecture detail urls 에서 작업을 해야하는 부분인가?

    def post(self, request, lecture_id):
        data = request.POST
        member = request.session.get('member')  # 세션에서 멤버 정보 가져오기
        if member:
            my_cart = Cart.objects.filter(member=member, cart_status=0).first()
            data = {
                'quantity': data.get('counted-number', 1),
                'cart': my_cart,
                'lecture_id': lecture_id,
                'date': data.get('date'),
                'time': data.get('time'),
                'kit': data.get('kit'),
                'cart_detail_status': 0,  # 장바구니 상세 상태를 게시중으로 설정
            }

            # 동일 품목이 있는지 검사
            existing_item = CartDetail.objects.filter(cart=my_cart, lecture_id=lecture_id).first()
            if existing_item:
                existing_item.quantity += 1  # 동일 품목이 있는 경우 수량 증가
                existing_item.save()
            else:
                # 동일 품목이 없는 경우 CartDetail 생성
                CartDetail.objects.create(**data)

            return redirect('cart')  # 장바구니 페이지로 이동
        else:
            # 로그인이 필요한 경우 로그인 페이지로 이동
            return redirect('login')  # 로그인 페이지의 URL로 수정 필요


class CartDetailView(View):
    # 장바구니 상세 페이지 구현 필요
    pass