from operator import itemgetter

from django.db import transaction
# noinspection PyInterpreter
from django.db.models import F, Count
from django.utils import timezone

from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from apply.models import Apply
from knowhow.models import KnowhowFile, KnowhowReply, Knowhow, KnowhowPlant, KnowhowReplyLike, KnowhowLike
from lecture.models import LectureReview, LectureProductFile, LecturePlant, Lecture
from member.models import Member, MemberAddress, MemberProfile
from member.serializers import MemberSerializer
from post.models import Post, PostFile, PostPlant, PostReply, PostReplyLike, PostLike
from teacher.models import Teacher


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
        is_member = Member.objects.filter(**member_data)

        if not is_member.exists():
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


# =====================================================================================================================
class MypageUpdateView(View):
    def get(self, request):
        member_id = request.session['member']['id']
        request.session['member'] = MemberSerializer(Member.objects.get(id=member_id)).data
        check = request.GET.get('check')
        member_files = MemberProfile.objects.filter(id = member_id).first()
        session_file = request.session['member_files'][0]['file_url']
        member_file = member_files.file_url
        context = {
            'check': check,
            'member_file': member_file,
            'memberProfile': session_file
        }
        return render(request, 'member/mypage/my_settings/user-info-update.html', context)

    def post(self, request):
        data = request.POST
        files = request.FILES.getlist('new-image')
        member_id = request.session['member']['id']

        member = Member.objects.get(id=member_id)
        member.member_name = data['member-name']
        member.updated_date = timezone.now()
        member.save(update_fields=['member_name', 'updated_date'])

        if files:
            for file in files:
                member_profile, created = MemberProfile.objects.get_or_create(member=member)
                member_profile.file_url = file
                member_profile.updated_date = timezone.now()
                member_profile.save()
        request.session['member_files'] = list(member.memberprofile_set.values('file_url'))

        return redirect("member:update")


# =====================================================================================================================
# 내 활동 모두보기 view
class MypageShowView(View):
    def get(self,request):
        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post = list(Post.objects.filter(member_id=member['id']))
        knowhow = list(KnowhowLike.objects.filter(member_id=member['id']))
        post_count = len(post) + len(knowhow)
        lecture_review = LectureReview.objects.filter(member_id=member['id'])
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like) + len(knowhowlike)
        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'post': post,
            'teacher': teacher,
            'post_count': post_count,
            'lecture_review':lecture_review,
            'like_count':like_count
        }
        return render(request,'member/mypage/my_profile/see-all.html',context)

# 내 활동 내 게시글 view
class MypagePostView(View):
    def get(self,request):
        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post = list(Post.objects.filter(member_id=member['id']))
        knowhow = list(KnowhowLike.objects.filter(member_id=member['id']))
        post_count = len(post) + len(knowhow)
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like) + len(knowhowlike)

        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'post': post,
            'teacher': teacher,
            'post_count': post_count,
            'like_count':like_count
        }
        return render(request,'member/mypage/my_profile/my-posts.html',context)


# 내 활동 내 댓글 view
class MypageReplyView(View):
    def get(self,request):

        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike =KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like)+len(knowhowlike)
        post_reply = list(PostReply.objects.filter(member_id=member['id']))
        knowhow_reply = list(KnowhowReply.objects.filter(member_id=member['id']))
        reply_count = len(post_reply)+len(knowhow_reply)


        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'teacher':teacher,
            'like_count':like_count,
            'reply_count':reply_count
        }
        return render(request,'member/mypage/my_profile/my-comments.html',context)

# 내 활동 내 리뷰 view
class MypageReviewView(View):
    def get(self,request):
        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post = list(Post.objects.filter(member_id=member['id']))
        knowhow = list(KnowhowLike.objects.filter(member_id=member['id']))
        post_count = len(post) + len(knowhow)
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like) + len(knowhowlike)
        lecture_reply = LectureReview.objects.filter(member_id=member['id'])

        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'post': post,
            'teacher': teacher,
            'like_count': like_count,
            'post_count': post_count,
            'lecture_reply':lecture_reply
        }
        return render(request,'member/mypage/my_profile/my-reviews.html',context)

# 내 활동 좋아요 view
class MypageLikesView(View):

    def get(self,request):
        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post = list(Post.objects.filter(member_id=member['id']))
        knowhow = list(KnowhowLike.objects.filter(member_id=member['id']))
        post_count = len(post) + len(knowhow)
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like) + len(knowhowlike)
        post_reply = list(PostReply.objects.filter(member_id=member['id']))
        knowhow_reply = list(KnowhowReply.objects.filter(member_id=member['id']))
        reply_count = len(post_reply) + len(knowhow_reply)

        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'post': post,
            'teacher': teacher,
            'like_count': like_count,
            'post_count': post_count,
            'reply_count': reply_count
        }

        return render(request,'member/mypage/my_profile/likes.html',context)

# 내 활동 스크랩북 강의 스크랩// 작업중
class MypageLectureScrapsView(View):

    def get(self,request):
        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = list(KnowhowLike.objects.filter(member_id=member['id']))
        like.extend(knowhowlike)
        like_count = len(like)

        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'teacher': teacher,
            'like_count' : like_count
        }
        return render(request,'member/mypage/my_profile/scrapbook/lecture-scrapbook.html',context)


# 내가 신청한 view // 작업중
class MypageLecturesView(View):
    def get(self, request):

        member = request.session['member']
        member_file = request.session['member_files']
        teacher = Teacher.objects.filter(member_id=member['id'])
        post_like = list(PostLike.objects.filter(member_id=member['id']))
        knowhowlike = KnowhowLike.objects.filter(member_id=member['id'])
        like_count = len(post_like) + len(knowhowlike)
        lecture = Apply.objects.filter(member_id = member['id'])
        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'teacher': teacher,
            'like_count': like_count,
            'lecture':lecture
        }
        return render(request,'member/mypage/my_lecture/my-lectures.html',context)


class LectureReviewView(View):
    def get(self, request, lecture_id):
        member = request.session['member']
        member_file = request.session['member_files']
        context = {
            'member': member,
            'memberProfile': member_file[0]['file_url'],
            'lecture_id':lecture_id
        }

        return render(request, 'member/mypage/my_lecture/write-lecture-review.html',context)

    @transaction.atomic
    def post(self, request, lecture_id):
        data = request.POST
        # 현재 로그인한 사용자
        member = request.session['member']

        print(data.values())
        data = {
            'review_content': data['content-input'],
            'member': Member.objects.get(id=member['id']),
            'lecture_id': lecture_id,
            'review_title': data['title-input'],
            'review_rating': data.get('rate')
        }

        LectureReview.objects.create(**data)

        return redirect('/member/mypage/lectures/')
# =====================================================================================================================
# API

# 포스트, 노하우 리스트 합본
# updated_date 기준 최신순 정렬
# 12개 한페이지
class MypagePostListAPI(APIView):
    def get(self, request, page):

        row_count = 12
        offset = (page - 1) * row_count
        limit = row_count * page

        posts = list(Post.objects.filter(member_id=request.session['member']['id'])\
            .annotate(member_name=F('member__member_name'))\
            .values(
                'id',
                'post_title',
                'post_content',
                'post_count',
                'member_name',
                'updated_date',
            ))

        for post in posts:
            post_file = PostFile.objects.filter(post_id=post['id']).values('file_url').first()
            if post_file is not None:
                post['post_file'] = post_file['file_url']
            else:
                post['post_file'] = 'file/2024/03/05/blank-image.png'

            tags = PostPlant.objects.filter(post_id=post['id']).values('plant_name')
            post['post_plant'] = [tag['plant_name'] for tag in tags]

            replies = PostReply.objects.filter(post_id=post['id']).values('id')
            post['post_reply'] = [reply['id'] for reply in replies]


        knowhows = list(Knowhow.objects.filter(member_id=request.session['member']['id']) \
            .annotate(writer=F('member__member_name')) \
            .values(
            'id',
            'knowhow_title',
            'knowhow_content',
            'knowhow_count',
            'writer',
            'updated_date',
        ))

        for knowhow in knowhows:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow['id']).values('file_url').first()
            if knowhow_file is not None:
                knowhow['knowhow_file'] = knowhow_file['file_url']
            else:
                knowhow['knowhow_file'] = 'file/2024/03/05/blank-image.png'

            tags = KnowhowPlant.objects.filter(knowhow_id=knowhow['id']).values('plant_name')
            knowhow['knowhow_plant'] = [tag['plant_name'] for tag in tags]

            replies = KnowhowReply.objects.filter(knowhow_id=knowhow['id']).values('id')
            knowhow['knowhow_reply'] = [reply['id'] for reply in replies]

        posts.extend(knowhows)
        # updated_date를 기준으로 최신순으로 정렬
        sorted_posts = sorted(posts, key=itemgetter('updated_date'), reverse=True)

        return Response(sorted_posts[offset:limit])



# 노하우 리스트
# 12개 한페이지
class MypageKnowhowListAPI(APIView):
    def get(self, request, page):

        row_count = 12
        offset = (page - 1) * row_count
        limit = row_count * page

        print('모든 리스트 가져오기 2')
        knowhows = Knowhow.objects.filter(member=request.session['member']['id'])\
            .annotate(writer=F('member__member_name'))\
            .values(
                'id',
                'knowhow_title',
                'knowhow_content',
                'knowhow_count',
                'writer',
                'updated_date',
            )

        for knowhow in knowhows:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow['id']).values('file_url').first()
            if knowhow_file is not None:
                knowhow['knowhow_file'] = knowhow_file['file_url']
            else:
                knowhow['knowhow_file'] = 'file/2024/03/05/blank-image.png'

            tags =KnowhowPlant.objects.filter(knowhow_id=knowhow['id']).values('plant_name')
            knowhow['knowhow_plant'] = [tag['plant_name'] for tag in tags]

            replies = KnowhowReply.objects.filter(knowhow_id=knowhow['id']).values('id')
            knowhow['knowhow_reply'] = [reply['id'] for reply in replies]

        return Response(knowhows[offset:limit])

# 노하우, 포스트 댓글 리스트 합본
# updated_date 기준 최신순 정렬
# 4개 한페이지
class MypageShowReplyAPI(APIView):
    def get(self, request, page):

        row_count = 4
        offset = (page - 1) * row_count
        limit = row_count * page


        post_replies = list(PostReply.objects.filter(member=request.session['member']['id'])\
            .annotate(
                member_name=F('member__member_name'),
                post_title=F('post__post_title'),
                post_writer=F('post__member__member_name'),
                post_count=F('post__post_count'),
                post_tag=F('post__posttag__tag_name'))\
            .values(
                'id',
                'post_id',
                'post_reply_content',
                'member_name',
                'updated_date',
                'post_title',
                'post_writer',
                'post_count',
                'post_tag'
            ))

        for post_reply in post_replies:
            post_file = PostFile.objects.filter(post_id=post_reply['post_id']).values('file_url').first()
            if post_file is not None:
                post_reply['post_file'] = post_file['file_url']
            else:
                post_reply['post_file'] = 'file/2024/03/05/blank-image.png'

            tags = PostPlant.objects.filter(post_id=post_reply['post_id']).values('plant_name')
            post_reply['post_plant'] = [tag['plant_name'] for tag in tags]

            likes = PostReplyLike.objects.filter(post_reply_id=post_reply['id']).values('id')
            post_reply['likes'] = [like['id'] for like in likes]


        knowhow_replies = list(KnowhowReply.objects.filter(member=request.session['member']['id']) \
            .annotate(
            member_name=F('member__member_name'),
            knowhow_title=F('knowhow__knowhow_title'),
            knowhow_writer=F('knowhow__member__member_name'),
            knowhow_count=F('knowhow__knowhow_count'),
            knowhow_tag=F('knowhow__knowhowtag__tag_name')) \
            .values(
            'id',
            'knowhow_id',
            'knowhow_reply_content',
            'member_name',
            'updated_date',
            'knowhow_title',
            'knowhow_writer',
            'knowhow_count',
            'knowhow_tag'
        ))

        for knowhow_reply in knowhow_replies:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow_reply['knowhow_id']).values('file_url').first()
            if knowhow_file is not None:
                knowhow_reply['knowhow_file'] = knowhow_file['file_url']
            else:
                knowhow_reply['knowhow_file'] = 'file/2024/03/05/blank-image.png'

            tags = KnowhowPlant.objects.filter(knowhow_id=knowhow_reply['knowhow_id']).values('plant_name')
            knowhow_reply['knowhow_plant'] = [tag['plant_name'] for tag in tags]

            likes = KnowhowReplyLike.objects.filter(knowhow_reply_id=knowhow_reply['id']).values('id')
            knowhow_reply['likes'] = [like['id'] for like in likes]

        post_replies.extend(knowhow_replies)
        sorted_posts_replies = sorted(post_replies, key=itemgetter('updated_date'), reverse=True)

        return Response(sorted_posts_replies[offset:limit])


# 강의 리뷰 리스트
# 5개 한페이지
class MypageShowReviewAPI(APIView):
    def get(self, request, page):

        row_count = 5
        offset = (page - 1) * row_count
        limit = row_count * page

        reviews = LectureReview.objects.filter(member=request.session['member']['id'])\
            .annotate(
                member_name=F('member__member_name'),
                lecture_title=F('lecture__lecture_title'),
                teacher_name=F('lecture__teacher__member__member_name'),
                lecture_category=F('lecture__lecture_category__lecture_category_name'))\
            .values(
                'id',
                'lecture_id',
                'lecture_title',
                'review_title',
                'review_content',
                'review_rating',
                'updated_date',
                'teacher_name',
                'lecture_category'
            )

        for review in reviews:
            lecture_file = LectureProductFile.objects.filter(lecture_id=review['lecture_id']).values('file_url').first()
            if lecture_file is not None:
                review['lecture_file'] = lecture_file['file_url']
            else:
                review['lecture_file'] = 'file/2024/03/05/blank-image.png'

            tags = LecturePlant.objects.filter(lecture_id=review['lecture_id']).values('plant_name')
            review['lecture_plant'] = [tag['plant_name'] for tag in tags]

        return Response(reviews[offset:limit])


# 포스트, 노하우 좋아요 리스트 합본
# 12개 한페이지
class MypageShowLikesAPI(APIView):
    def get(self, request,page):

        row_count = 12
        offset = (page - 1) * row_count
        limit = row_count * page


        likes = list(PostLike.objects.filter(member_id = request.session['member']['id']) \
            .annotate(
            member_name=F('member__member_name'),
            post_title=F('post__post_title'),
            post_writer=F('post__member__member_name'),
            post_count=F('post__post_count'),
            post_tag=F('post__posttag__tag_name')) \
            .values(
            'id',
            'post_id',
            'member_name',
            'updated_date',
            'post_title',
            'post_writer',
            'post_count',
            'post_tag'
        ))

        for like in likes:
            post_file = PostFile.objects.filter(post_id=like['post_id']).values('file_url').first()
            if post_file is not None:
                like['post_file'] = post_file['file_url']
            else:
                like['post_file'] = 'file/2024/03/05/blank-image.png'

            tags = PostPlant.objects.filter(post_id=like['post_id']).values('plant_name')
            like['post_plant'] = [tag['plant_name'] for tag in tags]


        knowhow_likes = list(KnowhowLike.objects.filter(member_id=request.session['member']['id']) \
            .annotate(
            member_name=F('member__member_name'),
            knowhow_title=F('knowhow__knowhow_title'),
            knowhow_writer=F('knowhow__member__member_name'),
            knowhow_count=F('knowhow__knowhow_count'),
            knowhow_tag=F('knowhow__knowhowtag__tag_name')) \
            .values(
            'id',
            'knowhow_id',
            'member_name',
            'updated_date',
            'knowhow_title',
            'knowhow_writer',
            'knowhow_count',
            'knowhow_tag'
        ))

        for knowhow_like in knowhow_likes:
            knowhow_file = KnowhowFile.objects.filter(knowhow_id=knowhow_like['knowhow_id']).values('file_url').first()
            if knowhow_file is not None:
                knowhow_like['knowhow_file'] = knowhow_file['file_url']
            else:
                knowhow_like['knowhow_file'] = 'file/2024/03/05/blank-image.png'

            tags = KnowhowPlant.objects.filter(knowhow_id=knowhow_like['knowhow_id']).values('plant_name')
            knowhow_like['knowhow_plant'] = [tag['plant_name'] for tag in tags]

        likes.extend(knowhow_likes)
        sorted_likes = sorted(likes, key=itemgetter('updated_date'), reverse=True)

        return Response(sorted_likes[offset:limit])

# 강의 수강 리스트 // 작업중
class MypageShowLecturesAPI(APIView):
    def get(self, request,page):
        row_count = 6
        offset = (page - 1) * row_count
        limit = row_count * page

        applies = Apply.objects.filter(member_id=request.session['member']['id']) \
            .annotate(
            member_name=F('member__member_name'),
            lecture_title=F('lecture__lecture_title'),
            teacher_name=F('lecture__teacher__member__member_name'),
            lecture_content=F('lecture__lecture_content'),
            lecture_category=F('lecture__lecture_category__lecture_category_name'),
            )\
            .values(
            'apply_status',
            'id',
            'lecture_id',
            'member_name',
            'updated_date',
            'lecture_title',
            'teacher_name',
            'lecture_content',
            'time',
            'date',
            'kit',
            'lecture_category'
        )

        for apply in applies:
            review = LectureReview.objects.filter(member_id=request.session['member']['id'], lecture_id=apply['lecture_id'])
            apply['lecture_review'] = review.values('id')

            lecture_file = LectureProductFile.objects.filter(lecture_id=apply['lecture_id']).values('file_url').first()
            if lecture_file is not None:
                apply['lecture_file'] = lecture_file['file_url']
            else:
                apply['lecture_file'] = 'file/2024/03/05/blank-image.png'

            tags = LecturePlant.objects.filter(lecture_id=apply['lecture_id']).values('plant_name')
            apply['lecture_plant'] = [tag['plant_name'] for tag in tags]
        sorted_applies = sorted(applies, key=itemgetter('date'), reverse=True)
        return Response(sorted_applies[offset:limit])