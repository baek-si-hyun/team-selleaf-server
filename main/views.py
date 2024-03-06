from datetime import timedelta, datetime

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

        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        knowhows = Knowhow.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'knowhow_count')[:11].values()

        start_of_day = datetime(today.year, today.month, today.day, 0, 0, 0)
        end_of_day = datetime(today.year, today.month, today.day, 23, 59, 59)
        trades = Trade.enabled_objects.filter(created_date__range=(start_of_day, end_of_day)).order_by('-id')[
                :7].values()

        posts = Post.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'post_count')[:4].values()

        lectures = Lecture.objects.order_by(
            'created_date')[:4].values()

        context = {
            'memberProfile': profile['file_url'],
            'knowhows': knowhows,
            'trades': trades,
            'posts': posts,
            'lectures': lectures

        }
        return render(request, 'main/main.html', context)
