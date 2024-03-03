from django.db import models

from lecture.models import Lecture
from member.models import Member
from selleaf.period import Period


class Apply(Period):
    APPLY_STATUS = [
        (0, '신청 완료'),
        (-1, '신청 취소'),
        (1, '수업 완료')
    ]

    apply_status = models.IntegerField(choices=APPLY_STATUS, default=0)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_apply'
        ordering = ['-id']


class Trainee(Period):
    trainee_name = models.CharField(null=False, blank=False, max_length=100)
    apply = models.ForeignKey(Apply, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_trainees'
        ordering = ['-id']
