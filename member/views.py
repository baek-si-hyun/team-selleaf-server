from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from member.serializers import MemberSerializer


class MemberCheckIdView(APIView):
    def get(self, request):
        member_id = request.GET['member-id']
        is_duplicated = Member.objects.filter(member_id=member_id).exists()
        return Response({'isDup': is_duplicated})


class MemberJoinView(View):
    def get(self, request):
        member_info = request.session['join-member-data']
        context = {
            'member_email': member_info['member_email'],
            'member_name': member_info['member_name']
        }
        return render(request, 'member/join/join.html', context)

    def post(self, request):
        post_data = request.POST
        marketing_agree = post_data.getlist('marketing-agree')
        marketing_agree = True if marketing_agree else False
        sms_agree = post_data.getlist('sms-agree')
        sms_agree = True if sms_agree else False
        member_info = request.session['join-member-data']

        data = {
            'member_email': member_info['member_email'],
            'member_name': member_info['member_name'],
            # 'address_city': post_data['address-city'],
            # 'address_district': post_data['address-district'],
            # 'address_detail': post_data['address-detail'],
            'marketing_agree': marketing_agree,
            'sms_agree': sms_agree
        }
        Member.objects.create(**data)

        return redirect('member:login')


class MemberLoginView(View):
    def get(self, request):
        return render(request, 'member/login/login.html')


class MemberLogoutView(View):
    def get(self, request):
        request.session.clear()
        return redirect('member:login')
