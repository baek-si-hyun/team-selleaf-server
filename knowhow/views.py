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


        # knowhow_recommend_urls = data['knowhow-recommend-url']
        # knowhow_recommend_contents = data['knowhow-recommend-content']




        print(data)
        # print(files)

        # 현재 로그인된 사람의 정보
        member = Member(**request.session['member'])
        # print(member)

        # # 카테고리
        # knowhowcategory = {
        #     'category_name': data['category-name']
        # }
        #
        # # 노하우
        # knowhow = {
        #     'knowhow_title': data['knowhow-title'],
        #     'knowhow_content': data['knowhow-content'],
        #     'member': member
        # }
        #

        #
        # # 노하우 태그
        # knowhowtag = {
        #     'tag_name': data['knowhow-tags'],
        #     'knowhow': knowhow
        # }
        #
        # # 노하우 추천
        # knowhowrecommend = {
        #     'recommend_url': data['knowhow-recommend-url'],
        #     'recommend_content': data['knowhow-recommend-content'],
        #     'knowhow': knowhow
        # }

        # knowhowdata = Knowhow.objects.create(**knowhow)
        # KnowhowPlant.objects.create(**knowhowplant)
        # KnowhowTag.objects.create(**knowhowtag)
        # KnowhowCategory.objects.create(**knowhowcategory)
        # KnowhowRecommend.objects.create(**knowhowrecommend)

        # # 노하우 식물종류
        plant_types = data.getlist('plant-type')

        for plant_type in plant_types:
            print(plant_type)
            KnowhowPlant.objects.create(knowhow=knowhowdata, plant_name=plant_type)

        for key in files:
            print(key)
            # KnowhowFile.objects.create(knowhow=knowhowdata, file_url=files[key])

        return redirect('/knowhow/detail')

class KnowhowDetailView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/knowhow-detail.html')

class KnowhowListView(View):
    pass