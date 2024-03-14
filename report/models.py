from django.db import models

from selleaf.models import Report
from trade.models import Trade


# 거래 신고
class TradeReport(Report):
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trade_report'
        ordering = ['-id']

# 강의 신고

# 노하우 신고

# 댓글 신고

# 포스트 신고