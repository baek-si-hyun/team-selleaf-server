from allauth.socialaccount.models import SocialAccount
from django.views import View
from django.shortcuts import render


class OAuthLoginView(View):
    def get(self, request):
        user = SocialAccount.objects.get(user=request.user)
        member_email = ""
        if user.provider == "google":
            member_email = user.extra_data.get("email")
        elif user.provider == "kakao":
            member_email = user.extra_data.get("kakao_account").get("email")
        elif user.provider == "naver":
            member_email = user.extra_data.get("email")
        print(member_email)
        return render(request, 'member/login/login.html')
