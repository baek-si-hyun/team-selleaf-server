from django.db.models import F, Q
from django.shortcuts import render
from django.views import View

from lecture.models import LectureProductFile, Lecture


class TeacherEntryView(View):
    def get(self, request):
        # 최근 생성된 강의 10개 가지고 오기
        lectures = Lecture.enabled_objects.all().values('lecture_title', 'id', 'teacher__member__member_name')[:10]
        #
        for lecture in lectures:
            lecture_photo = LectureProductFile.objects.filter(lecture_id=lecture['id']).values('file_url').first()
            lecture['lecture_photo'] = lecture_photo['file_url']

        context = {
            'lectures': lectures,
        }
        return render(request, 'teacher/teacher-entry.html', context)

class TeacherSubView(View):
    def get(self, request):
        return render(request, 'teacher/teacher-sub.html')