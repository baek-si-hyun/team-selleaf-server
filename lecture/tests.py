import random

from django.test import TestCase

from lecture.models import Lecture, LectureCategory, LecturePlant, LectureProductFile
from teacher.models import Teacher


class LectureTestCase(TestCase):
    lecture_category = []
    for i in range(50):
        data = {
            'lecture_category_name': f'강의카테고리{i}'
        }
        lecture_category.append(data)
    lecture_category = LectureCategory.objects.bulk_create(lecture_category)

    teacher_queryset = Teacher.objects.all()
    for i in range(50):
        lecture_data = {
            'lecture_price': random.randint(100000, 500000),
            'lecture_headcount': i,
            'lecture_title': f'강의 제목{i}',
            'lecture_content': f'강의 내용{i}',
            'lecture_category': f'노하우 제목{i}',
            'teacher': teacher_queryset[random.randint(0, len(teacher_queryset) - 1)],
        }
        lecture = Lecture.objects.create(**lecture_data)

        for j in range(1, 3):
            lecture = {
                'lecture': lecture,
                'plant': f'식물이름{j}'
            }
            LecturePlant.objects.create(**lecture)

        for j in range(1, 5):
            knowhow_file_data = {
                'lecture': lecture,
                'file_url': 'https://imagedelivery.net/4aEUbX05h6IovGOQjgkfSw/f3d07f4d-3eed-4101-f641-6651699ef400/public'
            }
            LectureProductFile.objects.create(**knowhow_file_data)
        knowhow_plant = {
            'knowhow': knowhow,
            'plant_name': '관엽식물'
        }
        KnowhowPlant.objects.create(**knowhow_plant)

        for j in range(1, 5):
            knowhow_recommend = {
                'recommend_url': f'https://qweqwe.com/qweqe{j}',
                'recommend_content': f'식물키우기 좋은 장비{j}',
                'knowhow': knowhow,
            }
            KnowhowRecommend.objects.create(**knowhow_recommend)

        for j in range(1, 5):
            knowhow_tag = {
                'tag_name': f'노하우를 공유합니다.{j}',
                'knowhow': knowhow,
            }
            KnowhowTag.objects.create(**knowhow_tag)
