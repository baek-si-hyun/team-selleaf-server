from django.db import models

from member.models import Member
from report.managers import ReportManager
from selleaf.period import Period


# 신고 사유 카테고리 테이블
class ReportCategory(Period):
    # 각 신고 사유 별 명칭
    report_category_name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'tbl_report_category'


# 신고 내역 테이블
class Report(Period):
    report_name = models.CharField(max_length=255, null=False, blank=False)
    # 신고 사유와 신고자 정보를 FK로 받아옴
    report_category = models.ForeignKey(ReportCategory, null=False, on_delete=models.PROTECT)
    member_id = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)
    # 신고사항 처리 상태 - 게시 중(1), 삭제됨(0)
    report_status = models.BooleanField(null=False, blank=False, default=True)
    # Managers
    objects = models.Manager()
    enabled_objects = ReportManager()

    class Meta:
        db_table = 'tbl_report'
        ordering = ['-id']
