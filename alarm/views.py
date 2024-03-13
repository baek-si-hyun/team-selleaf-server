from django.shortcuts import render
from django.views import View


class AlarmView(View):
    def get(self, request):
        return render(request,'/member/mypage/my_settings/notice.html')