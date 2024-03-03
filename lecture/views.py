from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')


class LectureDetailOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-online.html')

    # @transaction.atomic
    # def post(self, request):
    #     data = request.POST
    #
    #     member = Member(**request.session['member'])
    #
    #     data = {
    #
    #         'post_title': data['post-title'],
    #         'post_content': data['post-content'],
    #         'member': member
    #     }
    #     post = Post.objects.create(**data)
    #
    #     for file in files:
    #         PostFile.objects.create(post=post, path=file)
    #
    #     # for key in file:
    #     #     PostFile.objects.create(post=post, path=file[key])
    #
    #     return redirect(post.get_absolute_url())

class LectureDetailOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-offline.html')


class LectureTotalView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-total.html')


class LectureUploadOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')

    def post(self, request):
        return redirect('lecture:detail-online')

class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


