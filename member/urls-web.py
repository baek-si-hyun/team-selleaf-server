from django.urls import path

from member.views import MemberJoinView, MemberLoginView, MemberLogoutView, MypageUpdateView, MypagePostListAPI, \
    MypagePostView, MypageShowView, MypageKnowhowListAPI, MypageShowReplyAPI, MypageReplyView, MypageShowReviewAPI, \
    MypageReviewView, MypageShowLikesAPI, MypageLikesView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('mypage/update/',MypageUpdateView.as_view(), name='update'),
    path('mypage/show/', MypageShowView.as_view(),name='show'),
    path('mypage/posts/', MypagePostView.as_view(), name='mypost'),
    path('mypage/show/posts/<int:page>/', MypagePostListAPI.as_view()),
    path('mypage/show/knowhow/<int:page>/', MypageKnowhowListAPI.as_view()),
    path('mypage/show/replies/<int:page>/', MypageShowReplyAPI.as_view()),
    path('mypage/replies/', MypageReplyView.as_view()),
    path('mypage/show/reviews/<int:page>/', MypageShowReviewAPI.as_view()),
    path('mypage/reviews/', MypageReviewView.as_view()),
    path('mypage/likes/', MypageLikesView.as_view()),
    path('mypage/show/likes/<int:page>/', MypageShowLikesAPI.as_view()),
    # path('mypage/scraps/')
]
