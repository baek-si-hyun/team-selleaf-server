from django.db import models

from member.models import Member
from selleaf.period import Period


class Alarm(Period):
    sender = models.ForeignKey(Member, on_delete=models.PROTECT, null=True, related_name='sender')
    receiver = models.ForeignKey(Member, on_delete=models.PROTECT, null=True, related_name='receiver', blank=True)
    # 확인 True 미확인 False
    alarm_status = models.BooleanField(null=True, default=False)
    alarm_category = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'tbl_alarm'
