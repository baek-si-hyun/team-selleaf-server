from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import MainView
from selleaf.views import ManagerLoginView, ManagerLogoutView, MemberManagementView, WriteNoticeView

urlpatterns = [
    path('', MainView.as_view()),
    # path('admin/', admin.site.urls),
    path('admin/login/', ManagerLoginView.as_view(), name='manager-login'),
    path('admin/logout/', ManagerLogoutView.as_view(), name='manager-logout'),
    path('admin/member/', MemberManagementView.as_view(), name='manager-member'),
    path('admin/notice/write', WriteNoticeView.as_view(), name='notice-write'),
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
