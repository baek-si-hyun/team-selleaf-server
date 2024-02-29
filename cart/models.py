# from django.db import models
#
# from django.db import models
#
# class Cart(Period):
#     user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
#     # 0 진행중 1완료 -1 삭제
#     cart_status = models.IntegerField(null=False,blank=False,default=0)
#
#     class Meta:
#         db_table = 'tbl_cart'
#         ordering = ['-id']
#
# class CartDetail(Period):
#     cart = models.ForeignKey(Cart, on_delete=models.PROTECT,null=False, blank=False)
#     lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT,null=False, blank=False)
#     quantity = models.IntegerField(blank=False,null=False,default=0)
#     # 상품 등록 삭제 진행중
#     status = models.IntegerField(blank=False,null=False,default=0)