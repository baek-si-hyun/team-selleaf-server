from django.db import models


class Alarm(Period):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='reciever', blank=True)
    # 확인 True 미확인 False
    alarm_status = models.BooleanField(null=True, default=False)
    alarm_category = models.IntegerField(null=True, blank=False)

    class Meta:
        db_table = 'tbl_alarm'
        ordering = ['-id']


