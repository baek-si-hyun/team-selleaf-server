from django.urls import path

from notice.views import NoticeWebView

app_name = 'notice'

urlpatterns = [
    path('web/', NoticeWebView.as_view(), name='web')
]
