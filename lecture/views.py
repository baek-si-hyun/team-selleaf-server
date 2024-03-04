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



class LectureDetailOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-offline.html')


class LectureTotalView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-total.html')


class LectureUploadOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')

    # @transaction.atomic
    def post(self, request):
        upload_online_data = request.POST

        # 현재 작성하는 사람의 세션을 가져옴
        # member = request.session['member']

        # 강의 구분
        print(upload_online_data['product-index'])

        # 식물 종류
        plants = upload_online_data.getlist('plant-type')
        for key in plants:
            print(key)

        # 가격
        print(int(upload_online_data['price-input']))

        # 인원
        print(upload_online_data['member-input'])

        #



        # post = Post.objects.create(**data)


        # for key in file:
        #     PostFile.objects.create(post=post, path=file[key])

        return redirect('lecture:detail-online')

class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


