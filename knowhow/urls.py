from django.urls import path

from knowhow.views import KnowhowCreateView, KnowhowDetailView, KnowhowListView

app_name = 'knowhow'

# asd
urlpatterns = [
    # 노하우 작성
    path('create/', KnowhowCreateView.as_view(), name='create'),
    # 노하우 상세
    path('detail/', KnowhowDetailView.as_view(), name='detail'),
    # 노하우 목록
    path('list/', KnowhowListView.as_view(), name='list'),
]