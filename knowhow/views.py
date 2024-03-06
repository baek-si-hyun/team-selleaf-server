from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from knowhow.models import Knowhow, KnowhowFile, KnowhowPlant, KnowhowTag, KnowhowCategory, KnowhowRecommend, \
    KnowhowLike, KnowhowReply
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

        knowhowdata = Knowhow.objects.create(**knowhow)

        # 카테고리
        knowhowcategory = {
            'category_name': data['knowhow-categoty'],
            'knowhow': knowhowdata
        }

        KnowhowCategory.objects.create(**knowhowcategory)

        # 노하우 태그
        knowhowtag = {
            'tag_name': data['knowhow-tag'],
            'knowhow': knowhowdata
        }

        KnowhowTag.objects.create(**knowhowtag)

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
        return redirect(f'/knowhow/detail/?id={knowhowdata.id}')

class KnowhowDetailView(View):
    def get(self, request):
        knowhow = Knowhow.objects.get(id=request.GET['id'])
        knowhow_tags = KnowhowTag.objects.filter(knowhow_id__gte=1).values('tag_name')
        knowhow_likes = KnowhowLike.objects.filter(knowhow_id=knowhow.id)
        # for tag in knowhow_tags:
        #     print(tag)

        knowhow.knowhow_count += 1
        knowhow.save(update_fields=['knowhow_count'])

        knowhow_files = list(knowhow.knowhowfile_set.all())
        knowhow_file = list(knowhow.knowhowfile_set.all())[0]

        context = {
            'knowhow': knowhow,
            'knowhow_files': knowhow_files,
            'knowhow_file': knowhow_file,
            'knowhow_tags': knowhow_tags
        }

        # knowhow.post_read_count += 1
        # knowhow.updated_date = timezone.now()
        # post.save(update_fields=['post_read_count', 'updated_date'])

        return render(request, 'community/web/knowhow/knowhow-detail.html', context)



class KnowhowListView(View):
    pass

class KnowhowReplyWriteApi(APIView):
    @transaction.atomic
    def post(self, request):

        data = request.data
        print(data)
        data = {
            'knowhow_reply_content': data['reply_content'],
            'knowhow_id': data['knowhow_id'],
            'member_id': request.session['member']['id']
        }

        KnowhowReply.objects.create(**data)

        return Response('success')

class KnowhowReplyListApi(APIView):
    def get(self, request, knowhow_id, page):
        row_count = 5
        offset = (page - 1) * row_count
        limit = row_count * page

        replies = KnowhowReply.objects.filter(knowhow_id=knowhow_id).annotate(member_name=F('member__member_name'))\
            .values('member_name', 'knowhow__knowhow_content', 'member_id', 'created_date', 'id', 'knowhow_reply_content')

        return Response(replies[offset:limit])

class KnowhowReplyApi(APIView):
    pass