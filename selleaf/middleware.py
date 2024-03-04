from django.shortcuts import redirect


def pre_handle_request(get_response):
    def middleware(request):
        # 요청한 '상대 경로 + 쿼리 스트링' 을 변수에 할당
        uri = request.get_full_path()

        # 요청 경로를 잘 가져왔는지 검사
        print(uri)

        # 미들웨어에 작성한 코드가 반영되면 안되는 URI = 로그인 안 해도 이용 가능한 페이지들

        # 아래의 if문 분기들은 로그인이 필요한 페이지로 이동하려고 할 때 로그인 상태가 아니라면,
        # 로그인 페이지로 보내고, 로그인 이후에 원래 요청한 경로로 보내기 위한 목적임
        # 따라서 로그인이 필요한 서비스는 반드시 로그인 상태에서만 이용할 수 있게 됨

        # 만약 요청한 경로가 아래 서비스들(관리자, 계정, oAuth, API) 중 그 어느 것도 아니면서
        # 이 부분은 로그인 필요 없는 페이지들 추린 다음에 수정할 예정
        if 'admin' not in uri and 'accounts' not in uri and 'oauth' not in uri and 'api' not in uri:
            # 회원가입, 로그인 서비스도 아니고
            if 'join' not in uri and 'login' not in uri:
                # 로그인조차 하지 않은 상태라면
                if request.session.get('member') is None:
                    # 요청한 경로를 session에 담아놓은 뒤
                    request.session['previous_uri'] = uri
                    # 로그인 페이지로 이동시킨다
                    return redirect('/member/login')

            # 모바일 환경에서 요청을 했지만
            if request.user_agent.is_mobile:
                # 요청한 경로에 'mobile' 이라는 단어가 없으면
                if 'mobile' not in uri:
                    # 경로 앞에 'mobile' 이라는 단어를 붙이고
                    uri = f'/mobile{uri}'
                    # 'mobile' 이 붙은 경로(앱 경로)로 이동시킨다
                    return redirect(uri)

            # 모바일 환경에서 요청하지 않았는데
            else:
                # 경로에 'mobile' 이라는 단어가 붙어있다면
                if 'mobile' in uri:
                    # 경로 앞에 붙은 'mobile' 이라는 단어를 제거하고
                    uri = uri.replace('/mobile', '')
                    # 'mobile'이 빠진 경로(웹 경로)로 이동시킨다
                    return redirect(uri)

        # 응답 전처리
        response = get_response(request)

        # 응답 후처리
        return response

    return middleware
