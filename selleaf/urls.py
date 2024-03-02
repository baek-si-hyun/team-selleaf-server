from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('lecture/', include('lecture.urls')),
    path('order/', include('order.urls')),
    path('teacher/', include('teacher.urls')),
    path('trade/', include('trade.urls')),
    path('notice/', include('notice.urls')),
    path('qna/', include('qna.urls')),
    path('report/', include('report.urls')),
    path('knowhow/', include('knowhow.urls')),
    path('post/', include('post.urls')),
    path('cart/', include('cart.urls')),
    path('alarm/', include('alarm.urls')),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('oauth.urls')),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
