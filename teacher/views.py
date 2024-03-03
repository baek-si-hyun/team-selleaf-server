from django.shortcuts import render
from django.views import View


class TeacherEntryView(View):
    def get(self, request):
        return render(request, 'teacher/teacher-entry.html')

class TeacherSubView(View):
    def get(self, request):
        return render(request, 'teacher/teacher-sub.html')