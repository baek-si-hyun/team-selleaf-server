from django.urls import path

from post.views import PostCreateView

app_name = 'post'

urlpatterns = [
    # 포스트 작성
    path('create/', PostCreateView.as_view(), name='create'),

]
