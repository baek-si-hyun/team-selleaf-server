from datetime import timedelta, datetime

from django.db.models import F
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from knowhow.models import Knowhow
from lecture.models import Lecture
from post.models import Post
from trade.models import Trade


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
            'knowhow_count').annotate(member_profile=F('member__memberprofile__file_url')).annotate(member_name=F('member__member_name')).values('member_profile', 'member_name', 'id')
        for knowhow in knowhows:
            knowhow_file = Knowhow.objects.filter(id=knowhow['id']).values('knowhowfile__file_url').first()
            knowhow['knowhow_file_url'] = knowhow_file['knowhowfile__file_url']

        # 데이터가 너무 적어 하루단위를 일단 일주일 단위로 바꿈
        # start_of_day = datetime(today.year, today.month, today.day, 0, 0, 0)
        # end_of_day = datetime(today.year, today.month, today.day, 23, 59, 59)
        trades = Trade.enabled_objects.filter(created_date__range=(start_of_week, end_of_week)).order_by('-id').annotate(trade_category_name=F('trade_category__category_name')).values('id', 'trade_title', 'trade_content', 'trade_price', 'trade_category_name')[
                 :7]
        for trade in trades:
            trade_file = Trade.objects.filter(id=trade['id']).values('tradefile__file_url').first()
            trade['trade_file_url'] = trade_file['tradefile__file_url']

        posts = Post.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'post_count')[:4].values()

        # lectures = Lecture.objects.order_by(
        #     'created_date')[:4].values()
        # for lecture in lectures:
        #     lecture_file = Trade.objects.filter(id=lecture['id']).values('lecturefile__file_url').first()
        #     lecture['trade_file_url'] = lecture_file['lecturefile__file_url']
        # for lecture in lectures:
        #     print(lecture)


        context = {
            'memberProfile': profile['file_url'],
            'knowhows': knowhows,
            'trades': trades,
            # 'posts': posts,
            # 'lectures': lectures

        }
        return render(request, 'main/main.html', context)
