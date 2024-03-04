from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from knowhow.models import Knowhow, KnowhowFile, KnowhowPlant, KnowhowTag
from member.models import Member


class KnowhowCreateView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/create-knowhow.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        file = request.FILES

        print(data)
        # print(file)

        # 현재 로그인된 사람의 정보
        # member = Member(**request.session['member'])
        # print(member)

        # 아직 카테고리 테이블이 없음
        # knowhowcategory = {
        #
        # }


        # 노하우
        # knowhow = {
        #     'knowhow_title': data['knowhow-title'],
        #     'knowhow_content': data['knowhow-content'],
        #     'member': member
        # }

        # 노하우 식물분류
        # knowhowplant = {
        #     'plant_name': data['plant-name'],
        #     'knowhow':knowhow
        # }

        # 노하우 태그
        # knowhowtag = {
        #     'tag_name': data['knowhow-tags'],
        #     'knowhow': knowhow
        # }

        # knowhowdata = Knowhow.objects.create(**knowhow)
        # KnowhowPlant.objects.create(**knowhowplant)
        # KnowhowTag.objects.create(**knowhowtag)
        #
        for key in file:
            print('123')
            print(file[key])
        #     KnowhowFile.objects.create(post=knowhowdata, path=file[key])

        return redirect('/knowhow/detail')

class KnowhowDetailView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/knowhow-detail.html')

class KnowhowListView(View):
    pass