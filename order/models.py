from django.db import models

from lecture.models import Kit
from member.models import Member
from selleaf.models import Period, Address, Mileage


class Order(Period):
    ORDER_STATUS = [
        (0, '진행중'),
        (-1, '삭제'),
        (1, '결제완료')
    ]

    order_status = models.IntegerField(choices=ORDER_STATUS, default=0)
    order_receiver = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT, null=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-id']

class OrderMileage(Mileage):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = 'tbl_order_mileage'
        ordering = ['-id']
