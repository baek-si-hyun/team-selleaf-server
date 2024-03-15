from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from apply.models import Apply
from lecture.models import Lecture
from member.models import Member


class ApplyView(View):
    @transaction.atomic
    def post(self, request):
        apply_data = request.POST

        member = request.session['member']

        lecture = Lecture.objects.get(id=request.POST['lecture-id'])

        data = {
            'date': apply_data['date-input'],
            'time': apply_data['time-input'],
            'kit': apply_data['kit-input'],
            'member_id': member['member_id'],
            'lecture_id': lecture,
        }

        apply = Apply.objects.create(**data)

        return redirect()






