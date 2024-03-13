from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import MainView, KnowhowScrapAPI, TradeScrapAPI, LectureScrapAPI, PostScrapAPI, BestLectureCategoryAPI, \
    SearchView, SearchAPI, SearchHistoryAPI
from selleaf.views import ManagerLoginView, ManagerLogoutView, MemberManagementView, WriteNoticeView, \
    NoticeManagementView, UpdateNoticeView, DeleteNoticeView, WriteQnAView, QnAManagementView, \
    UpdateQnAView, DeleteQnAView, MemberInfoAPI, TeacherManagementView, TeacherInfoAPI, TeacherEntryManagementView, \
    TeacherEntriesInfoAPI, DeleteManyNoticeView, DeleteManyQnAView, DeleteManyMembersAPI, TeacherApprovalAPI, \
    TeacherDeleteAPI

urlpatterns = [
    path('', MainView.as_view()),
    path('search/', SearchView.as_view(), name='search'),
    path('search/api/', SearchAPI.as_view(), name='search-api'),
    path('search-history/api/', SearchHistoryAPI.as_view(), name='search-history-api'),
    path('knowhow-scrap/api/', KnowhowScrapAPI.as_view(), name='knowhow-scrap-api'),
    path('trade-scrap/api/', TradeScrapAPI.as_view(), name='trade-scrap-api'),
    path('lecture-scrap/api/', LectureScrapAPI.as_view(), name='lecture-scrap-api'),
    path('post-scrap/api/', PostScrapAPI.as_view(), name='post-scrap-api'),
    path('lecture-category/api/', BestLectureCategoryAPI.as_view(), name='lecture-category-api'),
    # 관리자 페이지 뷰
    path('admin/login/', ManagerLoginView.as_view(), name='manager-login'),
    path('admin/logout/', ManagerLogoutView.as_view(), name='manager-logout'),
    # 회원 관리
    path('admin/member/', MemberManagementView.as_view(), name='manager-member'),
    path('admin/member/<int:page>', MemberInfoAPI.as_view(), name='member-info'),
    path('admin/member/delete/<str:member_ids>', DeleteManyMembersAPI.as_view(), name='member-delete'),
    # 강사 및 강사 신청자 관리
    path('admin/teacher/', TeacherManagementView.as_view(), name='manager-teacher'),
    path('admin/teacher/<int:page>', TeacherInfoAPI.as_view(), name='teacher-info'),
    path('admin/teacher-entry/', TeacherEntryManagementView.as_view(), name='manager-teacher-entry'),
    path('admin/teacher-entry/<int:page>', TeacherEntriesInfoAPI.as_view(), name='teacher-entry-info'),
    path('admin/teacher-approve/<str:teacher_ids>', TeacherApprovalAPI.as_view(), name='teacher-entry-approval'),
    path('admin/teacher-delete/<str:teacher_ids>', TeacherDeleteAPI.as_view(), name='teacher-delete'),
    # 공지사항 관리
    path('admin/notice/', NoticeManagementView.as_view(), name='manager-notice'),
    path('admin/notice/write/', WriteNoticeView.as_view(), name='notice-write'),
    path('admin/notice/update/', UpdateNoticeView.as_view(), name='notice-update'),
    path('admin/notice/delete/', DeleteNoticeView.as_view(), name='notice-delete'),
    path('admin/notice/delete/<str:notice_ids>', DeleteManyNoticeView.as_view(), name='many-notice-delete'),
    # QnA 관리
    path('admin/qna/', QnAManagementView.as_view(), name='manager-qna'),
    path('admin/qna/write/', WriteQnAView.as_view(), name='qna-write'),
    path('admin/qna/update/', UpdateQnAView.as_view(), name='qna-update'),
    path('admin/qna/delete/', DeleteQnAView.as_view(), name='qna-delete'),
    path('admin/qna/delete/<str:qna_ids>', DeleteManyQnAView.as_view(), name='many-qna-delete'),
    # 기타 서비스 url
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