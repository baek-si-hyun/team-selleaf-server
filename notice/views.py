from django.shortcuts import render
from django.views import View


# 공지사항 페이지 이동 뷰
class NoticeWebView(View):
    def get(self, request):
        return render(request, 'notice/web/notice.html')
