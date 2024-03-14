from django.db.models import F
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from alarm.models import Alarm
from apply.models import Apply
from knowhow.models import Knowhow, KnowhowLike, KnowhowReply, KnowhowFile
from lecture.models import LectureReview, Lecture, LectureProductFile
from member.models import Member, MemberProfile
from post.models import PostLike, PostReply, PostFile


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
    def get(self, request, page):
        # 페이지당 알람 수와 오프셋, 리미트 계산
        row_count = 8
        offset = (page - 1) * row_count
        limit = page * row_count

        # 현재 멤버의 아이디 가져오기
        member_id = request.session['member']['id']

        # 멤버에게 전달된 알람들 가져오기
        alarms = Alarm.objects.filter(receiver=member_id).values()

        # 각 알람에 대한 추가 정보 처리
        for alarm in alarms:
            # 알람의 발신자 정보 가져오기
            sender = Member.objects.filter(id=alarm['sender_id']).first()
            alarm['sender'] = sender.member_name if sender else None

            # 발신자 파일 URL 가져오기 또는 기본값 설정
            sender_file = MemberProfile.objects.filter(member_id=alarm['sender_id']).values('file_url').first()
            alarm['member_file'] = sender_file['file_url'] if sender_file else 'file/2024/03/05/blank-image.png'

            # 알람 카테고리에 따라 메시지 생성
            # 1. ApplyAlarm
            if alarm['alarm_category'] == 1:

                applies = Apply.objects.filter(member_id=alarm['sender_id'], lecture__teacher_id=member_id, apply_status=0)\
                    .annotate(title=F('lecture__lecture_title')).values('title','lecture_id')

                for apply in applies:
                    target_file = LectureProductFile.objects.filter(id = apply['lecture_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    title = apply['title']
                    alarm["message"] = f'님이 {title} 강의를 신청하였습니다.'

            # 2. KnowhowLikeAlarm
            elif alarm['alarm_category'] == 2:

                knowhow_likes = KnowhowLike.objects.filter(member_id=alarm['sender_id'], knowhow__member_id=member_id)\
                    .annotate(knowhow_name=F('knowhow__knowhow_title')).values('knowhow_name','knowhow_id')

                for knowhow_like in knowhow_likes:
                    target_file = KnowhowFile.objects.filter(id=knowhow_like['knowhow_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    knowhow = [knowhow_like['knowhow_name']]
                    alarm["message"] = f'님이 {knowhow}를 좋아합니다.'

            # 3. KnowhowReplyAlarm
            elif alarm['alarm_category'] == 3:

                knowhow_replies = KnowhowReply.objects.filter(member_id=alarm['sender_id'],
                                                              knowhow__member_id=member_id) \
                    .annotate(knowhow_name=F('knowhow__knowhow_title')).values('knowhow_name').first()

                for knowhow_reply in knowhow_replies:
                    target_file = KnowhowFile.objects.filter(id=knowhow_reply['knowhow_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    knowhow = [knowhow_reply['knowhow_name']]
                    alarm["message"] = f'님이 {knowhow}에 댓글을 남겼습니다.'


            # 4. KnowhowReplyLikeAlarm
            elif alarm['alarm_category'] == 4:
                knowhow_replies = KnowhowReply.objects.filter(member_id=alarm['sender_id'],
                                                              knowhow__member_id=member_id) \
                    .annotate(knowhow_name=F('knowhow__knowhow_title'))
                print(knowhow_replies)
                for knowhow_reply in knowhow_replies:
                    target_file = KnowhowFile.objects.filter(id=knowhow_reply.knowhow_id).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    knowhow = knowhow_reply.knowhow_name
                    alarm["message"] = f'님이 {knowhow}에 남긴 댓글을 좋아합니다.'
                    alarm['reply'] = knowhow_reply.knowhow_reply_content

            # 5. PostLikeAlarm
            elif alarm['alarm_category'] == 5:

                post_likes = PostLike.objects.filter(member_id=alarm['sender_id'], post__member_id=member_id)\
                    .annotate(post_name=F('post__post_title')).values('post_name','post_id')

                for post_like in post_likes:
                    target_file = PostFile.objects.filter(id=post_like['post_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    post_like = [post_like['post_name']]
                    alarm["message"] = f'님이 {post_like}를 좋아합니다.'


            # 6. PostReplyAlarm
            elif alarm['alarm_category'] == 6:

                post_replies = PostReply.objects.filter(member_id=alarm['sender_id'],
                                                              post__member_id=member_id) \
                    .annotate(post_name=F('post__post_title')).values('post_name')
                for post_reply in post_replies:
                    target_file = PostFile.objects.filter(id=post_reply['post_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    post = [post_reply['post_name']]
                    alarm["message"] = f'님이 {post}에 댓글을 남겼습니다.'


            # 7. PostReplyLikeAlarm
            elif alarm['alarm_category'] == 7:
                post_replies = PostReply.objects.filter(member_id=alarm['sender_id'],
                                                              post__member_id=member_id) \
                    .annotate(post_name=F('post__post_title'))

                for post_reply in post_replies:
                    target_file = PostFile.objects.filter(id=post_reply.post_id).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    post = post_reply.post_name
                    alarm["message"] = f'님이 {post}에 남긴 댓글을 좋아합니다.'
                    alarm['reply'] = post_reply.post_reply_content

            # 8. ReviewAlarm
            elif alarm['alarm_category'] == 8:
                reviews = LectureReview.objects.filter(member_id=alarm['sender_id'], lecture__teacher_id=member_id)\
                    .annotate(lecture_name=F('lecture__lecture_title')).values('lecture_name','lecture_id')

                for review in reviews:
                    target_file = LectureProductFile.objects.filter(id=review['lecture_id']).values('file_url').first()
                    alarm['target_file'] = target_file['file_url'] if target_file else 'file/2024/03/05/blank-image.png'
                    review = review['lecture_name']
                    alarm["message"] = f'님이 {review}에 리뷰를 작성하였습니다.'

        # 처리된 알람 반환
        return Response(alarms[offset:limit])