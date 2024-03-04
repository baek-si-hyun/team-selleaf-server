from django.db import models

from selleaf.date import Date
from selleaf.period import Period


class Time(Period):
    time = models.TimeField(null=False, blank=False)
    date = models.ForeignKey(Date, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_time'
