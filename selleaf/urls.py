from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alarm/', include('alarm.urls')),
    path('apply/', include('apply.urls')),
    path('cart/', include('cart.urls')),
    path('knowhow/', include('knowhow.urls')),
    path('post/', include('post.urls')),
    path('mamber/', include('member.urls')),
    path('lecture/', include('lecture.urls')),
    path('notice/', include('notice.urls')),
    path('qna/', include('qna.urls')),
    path('report/', include('report.urls')),
    path('teacher/', include('teacher.urls')),
    path('trade/', include('trade.urls')),
    path('oauth/', include('oauth.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
