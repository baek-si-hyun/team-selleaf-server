from django.urls import path

from post.views import PostCreateView, PostDetailView, PostReplyWriteApi, PostDetailApi, PostReplyApi, PostScrapApi, \
    PostLikeApi, PostUpdateView, PostDeleteView, PostLikeCountApi

app_name = 'post'

urlpatterns = [
    # 포스트 작성
    path('create/', PostCreateView.as_view(), name='create'),
    # 포스트 상세
    path('detail/', PostDetailView.as_view(), name='detail'),
    # 포스트 수정
    path('update/', PostUpdateView.as_view(), name='update'),
    # 포스트 삭제
    path('delete/', PostDeleteView.as_view(), name='delete'),

    path('replies/write/', PostReplyWriteApi.as_view(), name='reply_write'),
    path('replies/list/<int:post_id>/<int:page>/', PostDetailApi.as_view(), name='reply_list'),
    path('replies/<int:reply_id>/', PostReplyApi.as_view()),

    path('scrap/<int:post_id>/<int:member_id>/<str:scrap_status>/', PostScrapApi.as_view()),
    path('like/<int:post_id>/<int:member_id>/<str:like_status>/', PostLikeApi.as_view()),
    path('like/count/<int:post_id>/', PostLikeCountApi.as_view()),
]
