# from django.db import models
#
# from notice.managers import NoticeManager
#
#
# class Notice(Period):
#     notice_title = models.CharField(max_length=255, null=False, blank=False)
#     notice_content = models.CharField(max_length=255, null=False, blank=False)
#
#     # 공지사항 게시 상태 - 게시 중(1), 삭제됨(0)
#     notice_status = models.BooleanField(null=False, blank=False, default=1)
#
#     # Managers
#     objects = models.Manager()
#     enabled_objects = NoticeManager()
#
#     class Meta:
#         db_table = 'tbl_notice'
#         ordering = ['-id']
