from django.contrib.auth.models import User
from django.db import models

from lecture.manager import LectureManager


class Lecture(Period):
    lecture_price = models.BigIntegerField(null=False, blank=False, default=0)
    lecture_headcount = models.IntegerField(null=False, blank=False, default=0)
    lecture_title = models.CharField(null=False, blank=False, max_length=100)
    lecture_content = models.CharField(null=False, blank=False, max_length=225)
    lecture_status = models.BooleanField(null=False, blank=False, default=False)
    lecture_category = models.ForeignKey(LectureCategory, on_delete=models.PROTECT)

    objects = models.Manager()
    enabled_objects = LectureManager()
    class Meta:
        db_table = 'tbl_lecture'
        ordering = ['-id']

class LectureCategory(Period):
    lecture_category_name = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        db_table = 'tbl_lecture_category'
        ordering = ['-id']

class LecturePlant(Period):
    plant_category = models.ForeignKey(PlantCategory, on_delete=models.PROTECT)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_lecture_plant'
        ordering = ['-id']

class LectureProductFile(File):
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_lecture_product_file'
        ordering = ['-id']

class LectureScrap(Scrap):
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_lecture_scrap'

class Kit(Period):
    kit_name = models.CharField(null=False, blank=False, max_length=100)
    kit_content = models.CharField(null=False, blank=False, max_length=225)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_kit'
        ordering = ['-id']


