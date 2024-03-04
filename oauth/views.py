from allauth.socialaccount.models import SocialAccount
from django.views import View
from django.shortcuts import render, redirect

from member.models import Member
from member.serializers import MemberSerializer


class OAuthLoginView(View):
    def get(self, request):
        user = SocialAccount.objects.get(user=request.user)
        oauth_data = user.extra_data
        if user.provider == "kakao":
            member_email = oauth_data.get("kakao_account").get("email")
            member_name = oauth_data.get("properties").get("nickname")
        else:
            member_email = oauth_data.get("email")
            member_name = oauth_data.get("name")

        data = {
            'member_email': member_email,
            'member_name': member_name,
        }
        member = Member.objects.filter(**data)

        url = '/'
        if member.exists():
            request.session['member'] = MemberSerializer(member.first()).data
        else:
            request.session['join-member-data'] = data
            url = "member:join"

        return redirect(url)
