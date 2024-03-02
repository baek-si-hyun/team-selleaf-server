from django.shortcuts import render
from django.views import View


class TeacherView(View):
    def get(self, request):
        return render(request, 'teacher/teacher-entry.html')
