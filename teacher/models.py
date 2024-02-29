from django.db import models

class Teacher(User):
    # 강사 약력
    teacher_info = models.CharField(max_length=50, blank=False, null=False)
    # 강의 설명
    lecture_info = models.CharField(max_length=100, blank=False, null=False)
    # 강의
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_teacher'
        ordering = ['-id']

class TeacherAddress(Address):
    # 강사
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_teacher_address'
        ordering = ['-id']

# 강의 품목 예시 테이블
class TeacherInfoFile(File):
    # 강사
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_teacher_info_file'
        ordering = ['-id']

# 강의 장소 사진 테이블
class TeacherPlaceFile(File):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_teacher_place_file'
        ordering = ['-id']