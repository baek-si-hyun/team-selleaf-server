from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice


# 관리자 로그인
class ManagerLoginView(View):
    # 관리자 로그인 페이지 이동 뷰
    def get(self, request):
        # 로그인 한 상태에서 다시 로그인 페이지에 접근하려 했는지 검사
        if request.session.get('admin') is not None:
            # 만약 그렇다면 회원 정보 리스트 페이지로 redirect
            return redirect('manager-member')

        # 로그인이 안 되어있던 상태라면 로그인 페이지로 이동
        return render(request, 'manager/login/login.html')

    # 관리자 로그인 버튼 누른 후의 뷰
    def post(self, request):
        # 로그인 정보를 가져옴
        data = request.POST

        # 관리자 로그인 정보도 'admin' 이라는 키로 세션에 저장
        request.session['admin'] = data

        # 이전에 요청한 관리자 페이지 내 경로가 있다면 변수에 담음
        previous_uri = request.session.get('previous_uri')

        # 따로 요청한 경로가 없을 때에는 회원 관리 페이지로 이동
        path = 'manager-member'

        # 만약 따로 요청한 페이지가 있었다면
        if previous_uri is not None:
            # 이동하려고 하는 경로를 요청한 페이지로 지정
            path = previous_uri

            # 원래 요청했던 페이지에 대한 정보는 세션에서 제거
            del request.session['previous_uri']

        # 위 분기에 따라 결정된 페이지로 이동
        # 기본적으로는 회원 관리 페이지
        return redirect(path)


# 관리자 로그아웃
class ManagerLogoutView(View):
    def get(self, request):
        # 세션 정보 전체 초기화
        request.session.clear()

        # 관리자 로그인 페이지로 이동
        return redirect('manager-login')


# 회원 관리
class MemberManagementView(View):
    # 회원관리 페이지 이동 뷰
    def get(self, request):
        # 모든 회원 정보를 가지고 가야됨(context)
        return render(request, 'manager/member/member/member.html')

    # 회원 삭제(status 변경) 눌렀을 때, 해당 정보를 업데이트하기 위한 뷰
    def post(self, request):
        return render(request, 'manager/member/member/member.html')


# 회원 상세 정보 관리(특정 회원 한 명)
class MemberDetailManagementView(View):
    # 특정 회원의 강의 구매 내역 페이지로 이동하기 위한 뷰
    # 결제 내역 관리 페이지가 따로 있기 때문에 상의 후 삭제할지 말지 결정
    def get(self, request):
        # 특정 회원의 정보와 강의 구매 내역을 join 해서 가지고 가야됨
        return render(request, 'manager/member/member-detail/member-detail.html')


# 강사 관리
class TeacherManagementView(View):
    # 강사 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 강사 정보를 가져가야 됨
        return render(request, 'manager/teacher/teacher.html')

    # 강사 정보(status) 변경 후, 해당 정보를 업데이트하기 위한 뷰
    def post(self, request):
        # status를 변경할 강사들의 정보를 가져와야 됨
        return render(request, 'manager/teacher/teacher.html')


# 게시물 관리
class PostManagementView(View):
    # 게시물 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 게시물(커뮤니티, 노하우, 거래) 정보 다 들고 가기
        return render(request, 'manager/post/post.html')

    # 게시물 삭제를 위한 뷰
    def post(self, request):
        # status를 변경할 게시물들의 정보를 가져와야 됨
        return render(request, 'manager/post/post.html')


# 강의 관리
class LectureManagementView(View):
    # 강의 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 강의에 대한 정보 필요
        return render(request, 'manager/lecture/lecture/lecture.html')

    # 특정 강의 삭제를 위한 뷰
    def post(self, request):
        return render(request, 'manager/lecture/lecture/lecture.html')


# 강의 리뷰 관리
class LectureReviewManagementView(View):
    # 강의 리뷰 관리 페이지 이동 뷰
    def get(self, request):
        # 특정 강의에 대한 모든 리뷰 정보 필요
        return render(request, 'manager/lecture/lecture/lecture.html')

    # 특정 리뷰 삭제를 위한 뷰
    def post(self, request):
        return render(request, 'manager/lecture/lecture/lecture.html')


# 댓글 관리
class ReplyManagementView(View):
    # 댓글 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 게시물에 대한 댓글을 전부 가져와야 됨
        return render(request, 'manager/comment/comment.html')

    # 특정 댓글 삭제를 위한 뷰
    def post(self, request):
        # 특정 댓글들 status 변경
        return render(request, 'manager/comment/comment.html')


# 태그 관리
class TagManagementView(View):
    # 태그 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 게시물에 대한 댓글을 전부 가져와야 됨
        return render(request, 'manager/tag/tag.html')

    # 특정 태그 삭제를 위한 뷰
    def post(self, request):
        # 태그들 status 변경
        return render(request, 'manager/tag/tag.html')


# 결제 내역 관리
class PaymentManagementView(View):
    # 결제 내역 관리 페이지 이동 뷰
    def get(self, request):
        # 모든 결제 내역과, 각 결제 내역의 회원, 상품 내역 전부 가져와야 됨
        return render(request, 'manager/payment/payment.html')


# 공지사항 관리
class NoticeManagementView(View):
    # 공지사항 내역 페이지 이동 뷰
    def get(self, request):
        # 공지사항 내역을 가져오는 것은 아래의 API가 해줌
        return render(request, 'manager/manager-notice/manager-notice/manager-notice.html')


class NoticeManagementAPI(APIView):
    # API에서 공지사항 목록을 가져오는 뷰
    # manager-notice.js에서 fetch로 요청받을 때 이 뷰가 사용된다
    def get(self, request, page):
        # 한 페이지 당 공지사항 최대 10개씩 표시
        row_count = 10

        # 한 페이지에 표시할 공지사항들을 슬라이싱 하기 위한 변수들
        offset = (page - 1) * row_count
        limit = page * row_count

        # 공지사항 표시에 필요한 tbl_notice의 컬럼들
        columns = [
            'id',
            'notice_title',
            'notice_content'
        ]

        # 게시 중인 공지사항의 제목과 내용을 10개씩 가져와서 notices에 할당(list)
        notices = Notice.enabled_objects.values(*columns)[offset:limit]

        # 다음 페이지에 표시할 공지사항이 있는지 판단하기 위한 변수
        # js로 페이지네이션을 구현하기 위함
        has_next_page = Notice.enabled_objects.filter()[limit:limit + 1].exists()

        # manager-notice.js에 보낼 공지사항 목록
        notice_info = {
            'notices': notices,
            'hasNext': has_next_page
        }

        # 요청한 목록 반환
        return Response(notice_info)


class WriteNoticeView(View):
    # 공지사항 작성 페이지 이동 뷰
    def get(self, request):
        # 로그인 검사는 미들웨어가 해주기 때문에, 별도의 정보 필요 없이 바로 render
        return render(request, 'manager/manager-notice/manager-notice/manager-notice-compose.html')

    # 공지사항 작성 완료 이후의 뷰
    @transaction.atomic
    def post(self, request):
        # POST 방식으로 요청한 데이터를 가져옴
        notice_data = request.POST

        # 받아온 데이터에서 특정 정보(id, 제목, 내용)를 가져와서 dict 타입으로 저장
        data = {
            'notice_title': notice_data['notice-title'],
            'notice_content': notice_data['notice-content'],
        }

        # 받아온 데이터로 tbl_notice에 실행할 insert 쿼리 작성
        Notice.objects.create(**data)

        # 작성한 공지사항 저장 후, 공지사항 리스트 페이지로 redirect
        return redirect('manager-notice')


class UpdateNoticeView(View):
    # 공지사항 수정 페이지 이동 뷰
    def get(self, request):
        # 수정할 공지사항 정보 가져오기
        return render(request, 'manager/manager-notice/manager-notice/manager-notice-modify.html')

    # 공지사항 수정 완료 이후의 뷰
    @transaction.atomic
    def post(self, request):
        # 기존 공지사항 정보 update 후, 공지사항 리스트 페이지로 redirect
        return redirect('/')


class DeleteNoticeView(View):
    # 공지사항 삭제를 위한 뷰
    def get(self, request):
        # 상태 업데이트 후, 공지사항 리스트 페이지로 redirect
        return redirect('manager-notice')


# QnA 관리
class QnAManagementView(View):
    # QnA 내역 페이지 이동 뷰
    def get(self, request):
        # 모든 QnA 전부 가져옴
        return render(request, 'manager/manager-notice/manager-qna/manager-qna.html')


class WriteQnAView(View):
    # QnA 작성 페이지 이동 뷰
    def get(self, request):
        # 로그인 검사는 미들웨어가 해주기 때문에, 별도의 정보 필요 없이 바로 render
        return render(request, 'manager/manager-notice/manager-qna/manager-qna-compose.html')

    # QnA 작성 완료 이후의 뷰
    @transaction.atomic
    def post(self, request):
        # 작성한 QnA 저장 후, QnA 리스트 페이지로 redirect
        return redirect('/')


class UpdateQnAView(View):
    # QnA 수정 페이지 이동 뷰
    def get(self, request):
        # 수정할 QnA 정보 가져오기
        return render(request, 'manager/manager-notice/manager-qna/manager-qna-modify.html')

    # QnA 수정 완료 이후의 뷰
    @transaction.atomic
    def post(self, request):
        # 기존 QnA 정보 update 후, QnA 리스트 페이지로 redirect
        return redirect('/')


class DeleteQnAView(View):
    # QnA 삭제를 위한 뷰
    def get(self, request):
        # 상태 업데이트 후, QnA 리스트 페이지로 redirect
        return redirect('/')


# 신고 내역 관리
class ReportManagementView(View):
    # 신고 내역 페이지 이동 뷰
    def get(self, request):
        # 신고 내역 전부 가져오기
        return render(request, 'manager/report/report.html')

    # 신고 내역 처리 or 삭제(반려) 후의 뷰
    # 이 페이지는 별도의 신고 상세 모달 또는 페이지를 제작하는 등의 개선이 필요해 보임
    def post(self, request):
        # update 완료 후, 다시 신고 내역 페이지로 이동
        return render(request, 'manager/report/report.html')

# 남은 것들
# 필요한 곳에 API 사용
# 내역 삭제 뷰 post 쓰지 말고 따로 분리할 지 회의
