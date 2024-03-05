from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from knowhow.models import Knowhow, KnowhowFile, KnowhowPlant, KnowhowTag, KnowhowCategory, KnowhowRecommend
from member.models import Member


class KnowhowCreateView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/create-knowhow.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        files = request.FILES

        # 현재 로그인된 사람의 정보
        member = Member(**request.session['member'])

        # 노하우
        knowhow = {
            'knowhow_title': data['knowhow-title'],
            'knowhow_content': data['knowhow-content'],
            'member': member
        }

        # 카테고리
        knowhowcategory = {
            'category_name': data['category-name'],
            'knowhow': knowhow
        }

        # 노하우 태그
        knowhowtag = {
            'tag_name': data['knowhow-tags'],
            'knowhow': knowhow
        }

        knowhowdata = Knowhow.objects.create(**knowhow)
        KnowhowTag.objects.create(**knowhowtag)
        KnowhowCategory.objects.create(**knowhowcategory)

        plant_types = data.getlist('plant-type')
        recommend_urls = data.getlist('knowhow-recommend-url')
        recommend_contents = data.getlist('knowhow-recommend-content')

        # 노하우 추천
        for i in range(len(recommend_urls)):
            KnowhowRecommend.objects.create(knowhow=knowhowdata, recommend_url=recommend_urls[i], recommend_content=recommend_contents[i])

        # 식물 종류
        for plant_type in plant_types:
            # print(plant_type)
            KnowhowPlant.objects.create(knowhow=knowhowdata, plant_name=plant_type)

        # 첨부파일
        for key in files:
            # print(key)
            KnowhowFile.objects.create(knowhow=knowhowdata, file_url=files[key])

        return redirect('/knowhow/detail')

class KnowhowDetailView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/knowhow-detail.html')

class KnowhowListView(View):
    pass