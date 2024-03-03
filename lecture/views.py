from django.shortcuts import render
from django.views import View


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')


class LectureDetailOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-online.html')


class LectureDetailOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-offline.html')


class LectureTotalView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-total.html')


class LectureUploadOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')


class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


