from django.utils import timezone

from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, MemberAddress, MemberProfile
from member.serializers import MemberSerializer


class MemberJoinView(View):
    def get(self, request):
        member = request.GET
        context = {
            'memberEmail': member['member_email'],
            'memberName': member['member_name'],
            'memberProfile': member['member_profile'],
            'memberType': member['member_type'],
        }
        return render(request, 'member/join/join.html', context)

    def post(self, request):
        post_data = request.POST
        marketing_agree = post_data.getlist('marketing-agree')
        marketing_agree = True if marketing_agree else False
        sms_agree = post_data.getlist('sms-agree')
        sms_agree = True if sms_agree else False

        member_data = {
            'member_email': post_data['member-email'],
            'member_name': post_data['member-name'],
            'member_type': post_data['member-type'],
            'marketing_agree': marketing_agree,
            'sms_agree': sms_agree
        }
        member = Member.objects.create(**member_data)

        profile_data = {
            'file_url': post_data['member-profile'],
            'member': member
        }
        MemberProfile.objects.create(**profile_data)

        address_data = {
            'address_city': post_data['address-city'],
            'address_district': post_data['address-district'],
            'address_detail': post_data['address-detail'],
            'member': member
        }
        MemberAddress.objects.create(**address_data)

        request.session['member'] = MemberSerializer(member).data
        member_files = list(member.memberprofile_set.values('file_url'))
        if len(member_files) != 0:
            request.session['member_files'] = member_files

        return redirect('/')


class MemberLoginView(View):
    def get(self, request):
        return render(request, 'member/login/login.html')


class MemberLogoutView(View):
    def get(self, request):
        request.session.clear()
        return redirect('member:login')

class MypageUpdateView(View):
    def get(self,request):

        request.session['member'] =MemberSerializer(Member.objects.get(id=request.session['member']['id'])).data
        check = request.GET.get('check')
        context = {'check': check}
        return render(request, 'member/mypage/my_settings/user-info-update.html', context)


    def post(self, request):
        data = request.POST
        file = request.FILES

        data = {
            'member_name': data['member-name'],
        }
        member = Member.objects.get(id=request.session['member']['id'])
        member_file = MemberProfile.objects.filter(member_id=member.id)

        if member_file.exists():
            member_file = member_file.first()

        else:
            member_file = MemberProfile(member=member)

        for key in file:
            member_file.path = file[key]
            member_file.updated_date = timezone.now()
            member_file.save()

        if data['member_password'] == member.member_password:
            member.member_name = data['member_name']
            member.updated_date = timezone.now()
            member.save(update_fields=['member_name', 'updated_date'])
            member_files = list(member.memberfile_set.values('path'))
            if len(member_files) != 0:
                request.session['member_files'] = member_files

            return redirect("member:mypage")

        return redirect("/member/mypage?check=false")