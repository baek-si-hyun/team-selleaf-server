from django.db import models

from member.models import Member
from selleaf.models import File


class Teacher(Member):
    # 강사 약력
    teacher_info = models.CharField(max_length=50, blank=False, null=False)
    # 강의 설명(앞으로 어떤 강의를 할지에 대한 설명)
    lecture_plan = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'tbl_teacher'
        ordering = ['-id']


# 강의 품목 예시 테이블
class TeacherInfoFile(File):
    # 강사
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_teacher_info_file'
        ordering = ['-id']
