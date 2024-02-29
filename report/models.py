from django.db import models

from report.managers import ReportManager


class Report(Period):
    report_name = models.CharField(max_length=255, null=False, blank=False)

    # 각 신고 사유를 id로 구분
    # 나중에 id 별 상세 정보를 담은 테이블이 필요?
    category = models.IntegerField(null=False, blank=False, default=0)
    user_id = models.ForeignKey(User, null=False, on_delete=models.PROTECT)

    # 신고사항 처리 상태 - 게시 중(1), 삭제됨(0)
    report_status = models.BooleanField(null=False, blank=False, default=1)

    # Managers
    objects = models.Manager()
    enabled_objects = ReportManager()

    class Meta:
        db_table = 'tbl_report'
        ordering = ['-id']
