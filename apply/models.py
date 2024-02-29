from django.db import models

from lecture.models import Lecture


class Apply(Period):
    APPLY_STATUS = [
        ('신청 완료', 0),
        ('신청 취소', -1),
        ('수업 완료', 1)
    ]

    apply_status = models.IntegerField(choices=APPLY_STATUS, default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_apply'
        ordering = ['-id']

class Trainee(Apply):
    trainee_name = models.CharField(null=False, blank=False, max_length=100)
    apply = models.ForeignKey(Apply, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_trainees'
        ordering = ['-id']
