from datetime import timedelta, datetime

from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework.views import APIView

from knowhow.models import Knowhow
from knowhow.serializers import KnowhowSerializer
from trade.models import Trade


class MainView(View):
    def get(self, request):
        member = request.session['member']
        profile = request.session['member_files'][0]
        context = {
            'memberProfile': profile['file_url']
        }
        return render(request, 'main/main.html', context)


class MainKnowhowAPI(APIView):
    def post(self, request):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        knowhows = Knowhow.objects.filter(created_date__range=(start_of_week, end_of_week)).order_by(
            'knowhow_count')[:11]

        knowhow_serializers = KnowhowSerializer(knowhows, many=True)

    # 강의 데이터 불러올 자리


class MainTradeAPI(APIView):
    def post(self, request):
        today = timezone.now().date()
        start_of_day = datetime(today.year, today.month, today.day, 0, 0, 0)
        end_of_day = datetime(today.year, today.month, today.day, 23, 59, 59)

        trade = Trade.enabled_objects.filter(created_date__range=(start_of_day, end_of_day)).order_by('-id')
