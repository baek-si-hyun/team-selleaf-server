from django.shortcuts import render
from django.views import View

from order.models import Order


class OrderView(View):
    # 카트 생성 확인 완료
    def get(self, request):

        # member = request.session['member']
        # member_file = request.session['member_files']
        # member_id = member.get('id')  # 멤버id 추출
        # my_order = Order.objects.filter(member_id=member_id, order_status=0)
        # if not my_order:
        #     # 장바구니가 없는 경우 새로운 장바구니 생성
        #     my_order = Order.objects.create(member_id=member_id)
        # else:
        #     my_order = my_order.first()

        # order_id = my_order.id
        # context = {
        #     'order_id': order_id,
        #     'memberProfile': member_file[0]['file_url'],
        #     'member': member
        # }

        return render(request, 'payment/payment.html')
