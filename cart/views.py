from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from cart.models import Cart, CartDetail
from member.models import Member


# 장바구니 서비스
class CartView(View):
    def get(self, request):
        member_data = request.session.get('member')  # 세션에서 멤버 정보 가져오기
        member_id = member_data.get('id')  # 멤버의 고유 식별자(ID) 추출
        print(member_id)
        my_cart = Cart.objects.filter(member_id=member_id, cart_status=0)
        if not my_cart:
            # 장바구니가 없는 경우 새로운 장바구니 생성
            my_cart = Cart.objects.create(member_id=member_id)
        else:
            my_cart = my_cart.first()

        cart_details = CartDetail.objects.filter(cart=my_cart)  # 장바구니 상세 정보 가져오기

        context = {
            'cart': my_cart,
            'cart_details': cart_details,
        }

        return render(request, 'cart/cart.html', context)


class CartUpdateView(View):
    # lecture detail 페이지에서 버튼을 누르면 정보입력

    def post(self, request, lecture_id):
        data = request.POST
        member = request.session.get('member')  # 세션에서 멤버 정보 가져오기
        if member:
            my_cart = Cart.objects.filter(member=member, cart_status=0).first()
            data = {
                'quantity': data.get('counted-number', 1),
                'cart': my_cart,
                'lecture': lecture_id,
                # 이 세부분 어떻게 가져오는 지 필요
                'date': data.get('date'),
                'time': data.get('time'),
                'kit': data.get('kit_id'),
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
            return redirect('member:login')  # 로그인 페이지의 URL로 수정 필요


class CartDeleteView(View):
    pass
    # # 장바구니 상세 페이지 구현 필요
    # cart_detail = CartDetail.objects.get(id=) # 이부분 어떻게 가져올지 필요
    # cart_detail.cart_status = -1
    # cart_detail.updated_date = timezone.now()
    # cart_detail.save(updated_fields=['updated_date','cart_status'])