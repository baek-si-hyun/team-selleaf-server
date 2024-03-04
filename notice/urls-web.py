from django.urls import path

from notice.views import NoticeView

app_name = 'notice'

urlpatterns = [
    path('web/', NoticeView.as_view(), name='web')
]
