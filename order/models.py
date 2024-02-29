from django.db import models

from lecture.models import Lecture


class Order(Period):
    ORDER_STATUS = [
        ('진행중', 0),
        ('삭제', -1),
        ('결제완료', 1)
    ]

    order_status = models.IntegerField(choices=ORDER_STATUS, default=0)
    order_receiver = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_order'
        ordering = ['-id']