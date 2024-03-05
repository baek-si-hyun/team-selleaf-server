import random

from django.test import TestCase

from cart.models import Cart
from member.models import Member


class CartTest(TestCase):
    member_queryset = Member.objects.all()
    cart_list = []
    for i in range(50):
        cart_data = {
            'lecture_price': random.randint(100000, 500000),
            'lecture_headcount': i,
            'lecture_title': f'강의 제목{i}',
            'lecture_content': f'강의 내용{i}',
            'cart_status': random.randint(-2, 1),
            'member': member_queryset[random.randint(0, len(member_queryset) - 1)],
        }
        cart_list.append(Cart(**cart_data))
    Cart.objects.create(cart_list)


    member_queryset = Member.objects.all()
