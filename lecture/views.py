from django.shortcuts import render
from django.views import View


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')