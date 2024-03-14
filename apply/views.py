from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from apply.models import Apply
from member.models import Member


class ApplyOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')

    @transaction.atomic
    def post(self, request):
        apply_data = request.POST

        member = request.session['member']

        data = {
            'date': apply_data['apply_date'],
            'time': apply_data['apply_time'],
            'kit': apply_data['kit'],
            'member_id': member['member_id'],
            'lecture_id': apply_data['lecture_id'],
        }

        apply = Apply.objects.create(**data)

        return redirect()






