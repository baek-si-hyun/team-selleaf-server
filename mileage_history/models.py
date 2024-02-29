from django.db import models

from lecture_review.models import Review
from selleaf.models import Mileage


class OrderMileage(Mileage):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT,null=False, blank=False)

    class Meta:
        db_table = 'tbl_order_mileage'
        ordering = ['-id']


class ReviewMileage(Mileage):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    review = models.ForeignKey(Review, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = 'tbl_review_mileage'
        ordering = ['-id']
