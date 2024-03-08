from django.urls import path

from knowhow.views import KnowhowCreateView, KnowhowDetailView, KnowhowReplyWriteApi, \
    KnowhowReplyListApi, KnowhowReplyApi, KnowhowListApi, KnowhowListView, KnowhowLikeApi, KnowhowReplyCountApi

app_name = 'knowhow'

# asd
urlpatterns = [
    # 노하우 작성
    path('create/', KnowhowCreateView.as_view(), name='create'),
    # 노하우 상세
    path('detail/', KnowhowDetailView.as_view(), name='detail'),
    # 노하우 목록
    path('list/', KnowhowListView.as_view(), name='list'),
    path('list/<int:page>', KnowhowListApi.as_view(), name='list'),

    # 댓글
    path('replies/write/', KnowhowReplyWriteApi.as_view(), name='reply_write'),
    path('replies/list/<int:knowhow_id>/<int:page>/', KnowhowReplyListApi.as_view(), name='reply_list'),
    path('replies/<int:reply_id>/', KnowhowReplyApi.as_view()),
    path('replies/count/<int:reply_id>/', KnowhowReplyCountApi.as_view()),

    # 좋아요
    path('knowhow/<int:knowhow_id>/<int:member_id>/', KnowhowLikeApi.as_view()),
]