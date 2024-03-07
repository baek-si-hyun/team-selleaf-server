from django.utils import timezone

from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response

from rest_framework.views import APIView

from cart.models import Cart, CartDetail
from member.models import Member


# 장바구니 서비스
class CartView(View):
    # 카트 생성 확인 완료
    def get(self, request):
        member_data = request.session.get('member')  # 세션에서 멤버 정보 가져오기
        member_id = member_data.get('id')  # 멤버id 추출
        my_cart = Cart.objects.filter(member_id=member_id, cart_status=0)
        if not my_cart:
            # 장바구니가 없는 경우 새로운 장바구니 생성
            my_cart = Cart.objects.create(member_id=member_id)
        else:
            my_cart = my_cart.first()

        cart_id = my_cart.id



        return render(request, 'cart/cart.html', {'cart_id':cart_id})


class CartListAPI(APIView):
    # lecture detail 페이지에서 버튼을 누르면 정보입력
    def get(self, request, cart_id):

        details = CartDetail.objects.filter(cart_id=cart_id,cart_detail_status=0)\
        .annotate(lecture_price=F('lecture__lecture_price')
                  ,lecture_title=F('lecture__lecture_title')
                  ,teacher_name=F('lecture__teacher__member__member_name')
                  ,lecture_files=F('lecture__lectureproductfile__file_url'))\
        .values('id','quantity', 'lecture_title','date','kit','time','teacher_name','lecture_price','lecture_files')

        return Response(details)



class CartAPI(APIView):
    def delete(self,request,detail_id):
        print(detail_id)
        detail = CartDetail.objects.filter(id=detail_id)
        detail.cart_detail_status = -1
        detail.updated_date = timezone.now()
        detail.save(update_fields=['cart_detail_status','updated_date'])
