from django.urls import path

from member.views import MemberJoinView, MemberLoginView, MemberLogoutView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout')
]
