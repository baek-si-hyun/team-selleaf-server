from django.db import models

from selleaf.models import Scrap, Period, Plant, File, Address
from trade.managers import TradeManager


class Trade(Period):
    TRADE_STATUS = [
        (True, '게시중'),
        (False, '게시취소')
    ]
    trade_price = models.IntegerField(null=False, blank=False, default=0)
    trade_title = models.CharField(null=False, blank=False, max_length=80)
    trade_content = models.CharField(null=False, blank=False, max_length=200)
    status = models.BooleanField(null=False, blank=False, default=True, choices=TRADE_STATUS)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    trade_category = models.ForeignKey(TradeCategory, on_delete=models.PROTECT, null=False)

    objects = models.Manager()
    enabled_objects = TradeManager()

    class Meta:
        db_table = 'tbl_trade'
        ordering = ['-id']


class TradeAddress(Address):
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trade_address'
        ordering = ['-id']


class TradeCategory(Period):
    category_name = models.CharField(null=False, blank=False, max_length=10)

    class Meta:
        db_table = 'tbl_trade_category'


class TradeFile(File):
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trade_file'


class TradePlant(Period):
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, null=False)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trade_plant'


class TradeScrap(Scrap):
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trade_scrap'
