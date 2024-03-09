from datetime import timedelta, datetime

from django.db.models import F, Count, Sum
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from knowhow.models import Knowhow, KnowhowFile, KnowhowScrap
from lecture.models import Lecture, LecturePlaceFile, LectureReview, LectureScrap, LecturePlant
from post.models import Post, PostScrap
from trade.models import Trade, TradeFile, TradeScrap
from lecture.serializers import LectureSerializer


class MainView(View):
    def get(self, request):
        member = request.session['member']
        profile = request.session['member_files'][0]

        if member is not None:
            profile = request.session['member_files'][0]
            context = {
                'memberProfile': profile['file_url']
            }

        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        knowhows = Knowhow.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'knowhow_count').annotate(member_profile=F('member__memberprofile__file_url'),
                                      member_name=F('member__member_name')).values('member_profile', 'member_name',
                                                                                   'id', 'knowhowscrap__status')[:10]
        for knowhow in knowhows:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow['id']).values('file_url').first()
            knowhow['knowhow_file_url'] = knowhow_file['file_url']

        # 데이터가 너무 적어 하루단위를 일단 일주일 단위로 바꿈
        # start_of_day = datetime(today.year, today.month, today.day, 0, 0, 0)
        # end_of_day = datetime(today.year, today.month, today.day, 23, 59, 59)
        trades = Trade.enabled_objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            '-id').annotate(trade_category_name=F('trade_category__category_name')).values('id', 'trade_title',
                                                                                           'trade_content',
                                                                                           'trade_price',
                                                                                           'trade_category_name',
                                                                                           'tradescrap__status')[:6]
        for trade in trades:
            trade_file = TradeFile.objects.filter(trade_id=trade['id']).values('file_url').first()
            trade['trade_file_url'] = trade_file['file_url']

        posts = Post.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'post_count').values()[:3]

        lectures = Lecture.enabled_objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            '-id').values('id', 'lecture_title', 'lecture_content', 'lecturescrap__status')[:4]
        for lecture in lectures:
            lecture_file = LecturePlaceFile.objects.filter(lecture_id=lecture['id']).values('file_url').first()
            lecture['lecture_file_url'] = lecture_file['file_url']

        # 데이터가 너무 적어 하루단위를 일단 일주일 단위로 바꿈
        lecture_reviews = LectureReview.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            '-id').annotate(lecture_title=F('lecture__lecture_title'), ).values('id', 'lecture_title', 'review_content',
                                                                                'lecture_id')[:3]
        for lecture_review in lecture_reviews:
            lecture_review_file = Lecture.objects.filter(id=lecture_review['lecture_id']).values(
                'lectureplacefile__file_url').first()
            lecture_review['lecture_file_url'] = lecture_review_file['lectureplacefile__file_url']

        best_lectures = Lecture.enabled_objects.order_by('-id').annotate(
            review_count=Count('lecturereview'),
            lecture_rating=(Sum('lecturereview__review_rating') / Count('lecturereview'))).values('id', 'lecture_title',
                                                                                                  'lecture_content',
                                                                                                  'lecturescrap__status',
                                                                                                  'review_count',
                                                                                                  'lecture_rating')[:3]

        for best_lecture in best_lectures:
            lecture_file = LecturePlaceFile.objects.filter(lecture_id=best_lecture['id']).values('file_url').first()
            best_lecture['lecture_file_url'] = lecture_file['file_url']
            tags = LecturePlant.objects.filter(lecture_id=best_lecture['id']).values('plant_name')
            best_lecture['lecture_tags'] = [tag['plant_name'] for tag in tags]
            if best_lecture['lecture_rating'] is None:
                best_lecture['lecture_rating'] = 0

        context = {
            'memberProfile': profile['file_url'],
            'knowhows': knowhows,
            'lectures': lectures,
            'trades': trades,
            'lectureReviews': lecture_reviews,
            'bestLectures': best_lectures
            # 'posts': posts,
        }
        return render(request, 'main/main.html', context)


class KnowhowScrapAPI(APIView):
    def patch(self, request):
        data = request.data
        data = {
            'knowhow_id': data['knowhow_id'],
            'member_id': request.session['member']['id']
        }

        knowhow_scrap, created = KnowhowScrap.objects.get_or_create(knowhow_id=data['knowhow_id'],
                                                                    member_id=data['member_id'])
        if not created:
            is_scrap = False if knowhow_scrap.status else True
            knowhow_scrap.status = is_scrap
            knowhow_scrap.save()

        return Response('success')


class TradeScrapAPI(APIView):
    def patch(self, request):
        data = request.data
        data = {
            'trade_id': data['trade_id'],
            'member_id': request.session['member']['id']
        }

        trade_scrap, created = TradeScrap.objects.get_or_create(trade_id=data['trade_id'], member_id=data['member_id'])
        if not created:
            is_scrap = False if trade_scrap.status else True
            trade_scrap.status = is_scrap
            trade_scrap.save()

        return Response('success')


class LectureScrapAPI(APIView):
    def patch(self, request):
        data = request.data
        data = {
            'lecture_id': data['lecture_id'],
            'member_id': request.session['member']['id']
        }

        lecture_scrap, created = LectureScrap.objects.get_or_create(lecture_id=data['lecture_id'],
                                                                    member_id=data['member_id'])
        if not created:
            is_scrap = False if lecture_scrap.status else True
            lecture_scrap.status = is_scrap
            lecture_scrap.save()

        return Response('success')


class PostScrapAPI(APIView):
    def patch(self, request):
        data = request.data
        data = {
            'post_id': data['post_id'],
            'member_id': request.session['member']['id']
        }

        post_scrap, created = PostScrap.objects.get_or_create(post_id=data['post_id'], member_id=data['member_id'])
        if not created:
            is_scrap = False if post_scrap.status else True
            post_scrap.status = is_scrap
            post_scrap.save()

        return Response('success')


class BestLectureCategoryAPI(APIView):
    def post(self, request):
        data = request.data
        catagory = data['category']
        best_lectures = Lecture.enabled_objects.filter(lectureplant__plant_name=catagory).annotate(
            review_count=Count('lecturereview'),
            lecture_rating=(Sum('lecturereview__review_rating') / Count('lecturereview'))).values('id', 'lecture_title',
                                                                                                  'lecture_content',
                                                                                                  'lecturescrap__status',
                                                                                                  'review_count',
                                                                                                  'lecture_rating')[:3]

        for best_lecture in best_lectures:
            lecture_file = LecturePlaceFile.objects.filter(lecture_id=best_lecture['id']).values('file_url').first()
            best_lecture['lecture_file_url'] = lecture_file['file_url']
            tags = LecturePlant.objects.filter(lecture_id=best_lecture['id']).values('plant_name')
            best_lecture['lecture_tags'] = [tag['plant_name'] for tag in tags]
            if best_lecture['lecture_rating'] is None:
                best_lecture['lecture_rating'] = 0

        # serializer = LectureSerializer(best_lectures, many=True).data
        # print(serializer)
        return Response(best_lectures)
