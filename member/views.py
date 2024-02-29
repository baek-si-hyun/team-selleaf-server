from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from member.serializers import MemberSerializer


class MemberCheckIdView(APIView):
    def get(self, request):
        member_id = request.GET['alarm-id']
        is_duplicated = Member.objects.filter(member_id=member_id).exists()
        return Response({'isDup': is_duplicated})


class MemberJoinView(View):
    def get(self, request):
        return render(request, 'member/join/join.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_name': data['alarm-name'],
            'member_birth': data['alarm-birth'],
            'member_phone': data['alarm-phone'],
            'member_id': data['alarm-id'],
            'member_password': data['alarm-password'],
            'member_email': data['alarm-email'],
        }

        member = Member.objects.create(**data)

        return redirect('member:login')


class MemberLoginView(View):
    def get(self, request):
        return render(request, 'member/login/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_id': data['alarm-id'],
            'member_password': data['alarm-password']
        }
        members = Member.objects.filter(member_id=data['member_id'], member_password=data['member_password'])
        if members.exists():
            request.session['alarm'] = MemberSerializer(members.first()).data
            # 메인 화면으로 가기
            return redirect('/post/list?page=1')

        return render(request, 'member/login/login.html', {'check': False})


