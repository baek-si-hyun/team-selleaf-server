from django.db.models import F
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from alarm.models import Alarm
from apply.models import Apply
from knowhow.models import Knowhow, KnowhowLike, KnowhowReply
from lecture.models import LectureReview
from member.models import Member


class AlarmView(View):
    def get(self, request):
        member = request.session['member']
        member_file = request.session['member_files']
        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
        }
        return render(request,'alarm/alarm.html', context)

class AlarmAPI(APIView):
    def get(self, request,page):

        row_count = 8
        offset = (page - 1) * row_count
        limit = page * row_count

        member_id = request.session['member']['id']
        alarms = Alarm.objects.filter(receiver=member_id).values()

        for alarm in alarms:
            sender = Member.objects.filter(id=alarm['sender_id']).first()
            alarm['sender']= sender.member_name
            if alarm['alarm_category'] == 1:
                applies = Apply.objects.filter(member_id=alarm['sender_id'], lecture__teacher_id=member_id, apply_status=0)\
                    .annotate(title = F('lecture__lecture_title')).values('title')
                for apply in applies:
                    title = apply['title']
                    alarm["message"] = f'님이 {title} 강의를 신청하였습니다.'
            elif alarm['alarm_category'] == 2:
                knowhow_likes = KnowhowLike.objects.filter(member_id=alarm['sender_id'], knowhow__member_id=member_id)\
                    .annotate(knowhow_name=F('knowhow__knowhow_title')).values('knowhow_name')
                for knowhow_like in knowhow_likes:
                    knowhow_like = [knowhow_like['knowhow_name']]
                    alarm["message"] = f'님이 {knowhow_like}를 좋아합니다.'
            elif alarm['alarm_category'] == 3:
                knowhow = KnowhowReply.objects.filter(member_id=alarm['sender_id'], knowhow__member_id=member_id)\
                    .annotate(knowhow_name=F('knowhow__knowhow_title')).values('knowhow_name', 'knowhow_reply_content')
                alarm["message"] = f'님이 {knowhow.knowhow_name}에 댓글을 남겼습니다.'
            elif alarm['alarm_category'] == 8:
                reviews = LectureReview.objects.filter(member_id=alarm['sender_id'], lecture__teacher_id=member_id)\
                .annotate(lecture_name = F('lecture__lecture_title')).values('lecture_name')
                for review in reviews:
                    review = review['lecture_name']
                    alarm["message"] = f'님이 {review}에 리뷰를 작성하였습니다.'

        return Response(alarms[offset:limit])