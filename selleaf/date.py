from django.db import models

from selleaf.period import Period


class Date(Period):
    date = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'tbl_date'
