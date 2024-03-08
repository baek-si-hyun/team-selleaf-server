from django.urls import path

from member.views import MemberJoinView, MemberLoginView, MemberLogoutView, MypageUpdateView, MypagePostListAPI, \
    MypagePostView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('update/',MypageUpdateView.as_view(), name='update'),
    path('mypage/myposts/', MypagePostView.as_view(), name='mypost'),
    path('mypage/myposts/<>', MypagePostListAPI.as_view())
]
