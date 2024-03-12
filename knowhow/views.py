from datetime import timedelta

from django.db import transaction
from django.db.models import F, Count, Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from knowhow.models import Knowhow, KnowhowFile, KnowhowPlant, KnowhowTag, KnowhowCategory, KnowhowRecommend, \
    KnowhowLike, KnowhowReply, KnowhowScrap
from member.models import Member, MemberProfile


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
        recommend_contents = data.getlist('knowhow-recommend-content')
        recommend_urls = data.getlist('knowhow-recommend-url')

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
        print(knowhow.__dict__)

        knowhow_tags = KnowhowTag.objects.filter(knowhow_id__gte=1).values('tag_name')
        reply_count = KnowhowReply.objects.filter(knowhow_id=knowhow.id).values('id').count()
        member_profile = MemberProfile.objects.filter(id=knowhow.member_id).values('file_url')




        knowhow.knowhow_count += 1
        knowhow.save(update_fields=['knowhow_count'])

        knowhow_files = list(knowhow.knowhowfile_set.all())
        knowhow_file = list(knowhow.knowhowfile_set.all())[0]


        print(knowhow)


        context = {
            'knowhow': knowhow,
            'knowhow_files': knowhow_files,
            'knowhow_file': knowhow_file,
            'knowhow_tags': knowhow_tags,
            'reply_count': reply_count,
            'member_profile': member_profile
        }

        return render(request, 'community/web/knowhow/knowhow-detail.html', context)

class KnowhowUpdateView(DetailView):
    def get(self, request):
        knowhow_id = request.GET.get('id')

        knowhow = Knowhow.objects.get(id=knowhow_id)
        knowhow_file = list(knowhow.knowhowfile_set.values('file_url'))
        # test = KnowhowFile.objects.filter(knowhow_id=knowhow_id).delete()
        # print(test)

        context = {
            'knowhow': knowhow,
            'knowhow_files': knowhow_file
        }

        return render(request, 'community/web/knowhow/edit-knowhow.html', context)

    @transaction.atomic
    def post(self, request):
        datas = request.POST
        files = request.FILES

        knowhow_id = request.GET['id']

        print(knowhow_id)
        print(datas)

        # test = KnowhowFile.objects.filter(knowhow_id=knowhow_id).delete()
        # print(test)

        # 지금 시간
        time_now = timezone.now()

        # 수정할 노하우 게시글 아이디
        knowhow = Knowhow.objects.get(id=knowhow_id)

        # 노하우 게시글 수정
        knowhow.knowhow_title = datas['knowhow-title']
        knowhow.knowhow_content = datas['knowhow-content']
        knowhow.updated_date = time_now
        knowhow.save(update_fields=['knowhow_title', 'knowhow_content', 'updated_date'])

        # 노하우 카테고리 수정
        knowhow_category = KnowhowCategory.objects.get(knowhow_id=knowhow_id)

        knowhow_category.category_name = datas['knowhow-category']
        knowhow_category.updated_date = time_now
        knowhow_category.save(update_fields=['category_name', 'updated_date'])

        # 노하우 식물종류 수정
        plant_types = datas.getlist('plant-type')

        KnowhowPlant.objects.filter(knowhow_id=knowhow_id).delete()

        for plant_type in plant_types:
            # print(plant_type)
            KnowhowPlant.objects.create(knowhow_id=knowhow_id, plant_name=plant_type, updated_date=time_now)

        # 노하우 태그 수정
        knowhow_tag = KnowhowTag.objects.get(knowhow_id=knowhow_id)

        knowhow_tag.tag_name = datas['knowhow-tag']
        knowhow_tag.updated_date = timezone.now()
        knowhow_tag.save(update_fields=['tag_name', 'updated_date'])

        # 노하우 추천 내용 수정
        recommend_contents = datas.getlist('knowhow-recommend-content')
        recommend_urls = datas.getlist('knowhow-recommend-url')

        KnowhowRecommend.objects.filter(knowhow_id=knowhow_id).delete()

        # 노하우 추천
        for i in range(len(recommend_urls)):
            KnowhowRecommend.objects.create(knowhow_id=knowhow_id, recommend_url=recommend_urls[i],
                                            recommend_content=recommend_contents[i])

        KnowhowFile.objects.filter(knowhow_id=knowhow_id).delete()

        for key in files:
            KnowhowFile.objects.create(knowhow_id=knowhow_id, file_url=files[key])

        return redirect(f'/knowhow/detail/?id={knowhow_id}')

class KnowhowDeleteView(View):
    @transaction.atomic
    def get(self, request):
        knowhow_id = request.GET['id']
        print(knowhow_id)
        KnowhowTag.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowFile.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowRecommend.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowReply.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowCategory.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowPlant.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowScrap.objects.filter(knowhow_id=knowhow_id).delete()
        KnowhowLike.objects.filter(knowhow_id=knowhow_id).delete()
        Knowhow.objects.filter(id=knowhow_id).delete()

        return redirect(f'/knowhow/list/')


class KnowhowListView(View):
    def get(self, request):

        knowhow_count = Knowhow.objects.count()

        context = {
            'knowhow_count': knowhow_count
        }

        return render(request, 'community/web/knowhow/knowhow.html', context)

class KnowhowListApi(APIView):
    def get(self, request, page, sorting, filters, type):
        row_count = 6
        offset = (page - 1) * row_count
        limit = row_count * page

        print(type)

        condition = Q()
        sort1 = '-id'
        sort2 = '-id'

        if type == '식물 키우기':
            condition |= Q(knowhowcategory__category_name__contains='식물 키우기')
        elif type == '제품 추천':
            condition |= Q(knowhowcategory__category_name__contains='제품 추천')
        elif type == '스타일링':
            condition |= Q(knowhowcategory__category_name__contains='스10')
        elif type == '전체':
            condition |= Q()

        filters = filters.split(',')
        for filter in filters:
            # print(filter.replace(',', ''))
            if filter.replace(',', '') == '관엽식물':
                condition |= Q(knowhowplant__plant_name__contains='관엽식물')

            elif filter.replace(',', '') == '침엽식물':
                condition |= Q(knowhowplant__plant_name__contains='침엽식물')

            elif filter.replace(',', '') == '희귀식물':
                condition |= Q(knowhowplant__plant_name__contains='희귀식물')

            elif filter.replace(',', '') == '다육':
                condition |= Q(knowhowplant__plant_name__contains='다육')

            elif filter.replace(',', '') == '선인장':
                condition |= Q(knowhowplant__plant_name__contains='선인장')

            elif filter.replace(',', '') == '기타':
                condition |= Q(knowhowplant__plant_name__contains='기타')

            elif filter.replace(',', '') == '전체':
                condition = Q()

        print(condition)

        if sorting == '최신순':
            sort1 = '-id'
            sort2 = '-created_date'

        elif sorting == '인기순':
            sort1 = '-like_count'
            sort2 = '-knowhow_count'

        elif sorting == "스크랩순":
            sort1 = '-scrap_count'
            sort2 = '-id'

        columns = [
            'knowhow_title',
            'member_name',
            'knowhow_count',
            'id',
            'member_id'
        ]

        # select_related로 조인먼저 해준다음, annotate로 member 조인에서 가져올 values 가져온다음
        # like와 scrap의 갯수를 가상 컬럼으로 추가해서 넣어주고, 진짜 사용할 밸류들 가져온 후, distinct로 중복 제거
        knowhows = Knowhow.objects.select_related('knowhowlike', 'knowhowscrap').filter(condition) \
            .annotate(member_name=F('member__member_name')) \
            .values(*columns) \
            .annotate(like_count=Count('knowhowlike'), scrap_count=Count('knowhowscrap')) \
            .values('knowhow_title', 'member_name', 'knowhow_count', 'id', 'member_id', 'like_count',
                    'scrap_count')\
            .order_by(sort1, sort2).distinct()

        # knowhow에 knowhow_file을 가상 컬럼을 만들어서 하나씩 추가해줌
        for knowhow in knowhows:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow['id']).values('file_url').first()
            profile = MemberProfile.objects.filter(member_id=knowhow['member_id']).values('file_url').first()
            knowhow['knowhow_file'] = knowhow_file['file_url']
            knowhow['profile'] = profile['file_url']

        # print(knowhows)

        return Response(knowhows[offset:limit])


class KnowhowReplyWriteApi(APIView):
    @transaction.atomic
    def post(self, request):

        data = request.data
        # print(data)
        data = {
            'knowhow_reply_content': data['reply_content'],
            'knowhow_id': data['knowhow_id'],
            'member_id': request.session['member']['id']
        }

        KnowhowReply.objects.create(**data)



        return Response('success')

class KnowhowDetailApi(APIView):
    def get(self, request, knowhow_id, page):
        member = request.session['member']

        row_count = 5
        offset = (page - 1) * row_count
        limit = row_count * page

        # 댓글 갯수
        reply_count = KnowhowReply.objects.filter(knowhow_id=knowhow_id).count()
        # 좋아요 갯수
        like_count = KnowhowLike.objects.filter(knowhow_id=knowhow_id).count()
        # 스크랩 갯수
        scrap_count = KnowhowScrap.objects.filter(knowhow_id=knowhow_id).count()
        # 게시글 작성 날짜
        knowhow_date = Knowhow.objects.filter(id=knowhow_id).values('created_date')



        replies = KnowhowReply.objects\
            .filter(knowhow_id=knowhow_id).annotate(member_name=F('member__member_name'))\
            .values('member_name', 'knowhow__knowhow_content', 'member_id', 'created_date', 'id', 'knowhow_reply_content')[offset:limit]

        data = {
            'replies': replies,
            'reply_count': reply_count,
            'knowhow_date': knowhow_date,
            'like_count': like_count,
            'scrap_count': scrap_count
        }

        return Response(data)

class KnowhowReplyApi(APIView):
    def delete(self, request, reply_id):
        KnowhowReply.objects.filter(id=reply_id).delete()
        return Response('success')

    def patch(self, request, reply_id):
        # print(request)
        reply_content = request.data['reply_content']
        updated_date = timezone.now()

        reply = KnowhowReply.objects.get(id=reply_id)
        reply.knowhow_reply_content = reply_content
        reply.updated_date = updated_date
        reply.save(update_fields=['knowhow_reply_content', 'updated_date'])

        return Response('success')

class KnowhowLikeScrapApi(APIView):
    def get(self, request, knowhow_id, member_id, status):
        pass