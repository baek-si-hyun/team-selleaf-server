from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import MainView, KnowhowScrapAPI, TradeScrapAPI, LectureScrapAPI, PostScrapAPI, BestLectureCategoryAPI, \
    SearchView
from selleaf.views import ManagerLoginView, ManagerLogoutView, MemberManagementView, WriteNoticeView, \
    NoticeManagementView, NoticeManagementAPI, UpdateNoticeView, DeleteNoticeView, WriteQnAView, QnAManagementView, \
    QnAManagementAPI, UpdateQnAView, DeleteQnAView

urlpatterns = [
    path('', MainView.as_view()),
    path('search/', SearchView.as_view(), name='search'),
    path('knowhow-scrap/api/', KnowhowScrapAPI.as_view(), name='knowhow-scrap-api'),
    path('trade-scrap/api/', TradeScrapAPI.as_view(), name='trade-scrap-api'),
    path('lecture-scrap/api/', LectureScrapAPI.as_view(), name='lecture-scrap-api'),
    path('post-scrap/api/', PostScrapAPI.as_view(), name='post-scrap-api'),
    path('lecture-category/api/', BestLectureCategoryAPI.as_view(), name='lecture-category-api'),
    # 관리자 페이지 뷰
    path('admin/login/', ManagerLoginView.as_view(), name='manager-login'),
    path('admin/logout/', ManagerLogoutView.as_view(), name='manager-logout'),
    path('admin/member/', MemberManagementView.as_view(), name='manager-member'),
    path('admin/notice/', NoticeManagementView.as_view(), name='manager-notice'),
    path('admin/notice/<int:page>', NoticeManagementAPI.as_view(), name='manager-notice-api'),
    path('admin/notice/write/', WriteNoticeView.as_view(), name='notice-write'),
    path('admin/notice/update/', UpdateNoticeView.as_view(), name='notice-update'),
    path('admin/notice/delete/', DeleteNoticeView.as_view(), name='notice-delete'),
    path('admin/qna/', QnAManagementView.as_view(), name='manager-qna'),
    path('admin/qna/<int:page>', QnAManagementAPI.as_view(), name='manager-qna-api'),
    path('admin/qna/write/', WriteQnAView.as_view(), name='qna-write'),
    path('admin/qna/update/', UpdateQnAView.as_view(), name='qna-update'),
    path('admin/qna/delete/', DeleteQnAView.as_view(), name='qna-delete'),
    path('member/', include('member.urls-web')),
    path('lecture/', include('lecture.urls-web')),
    path('order/', include('order.urls-web')),
    path('teacher/', include('teacher.urls-web')),
    path('trade/', include('trade.urls-web')),
    path('notice/', include('notice.urls-web')),
    path('qna/', include('qna.urls-web')),
    path('report/', include('report.urls-web')),
    path('knowhow/', include('knowhow.urls-web')),
    path('post/', include('post.urls-web')),
    path('cart/', include('cart.urls-web')),
    path('alarm/', include('alarm.urls-web')),
    path('oauth/', include('oauth.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)