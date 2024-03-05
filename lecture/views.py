from datetime import datetime, timedelta

from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')


class LectureDetailOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-online.html')



class LectureDetailOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-detail-offline.html')


class LectureTotalView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-total.html')


class LectureUploadOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')

    def date_range_with_weekdays(self, start, end, weekday_type):
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")

        # 요일 타입 가져오기
        weekdays = list(map(int, weekday_type))

        target_weekday_numbers = [weekday % 7 for weekday in weekdays]

        dates = []
        for target_weekday_number in target_weekday_numbers:
            # 시작 날짜로부터 요일까지의 차이
            start_weekday_difference = (target_weekday_number - start_date.weekday() + 7) % 7

            # 시작 날짜에 차이를 더해서 해당 요일의 첫 번째 날짜를 구함
            target_date = start_date + timedelta(days=start_weekday_difference)

            while target_date <= end_date:
                dates.append(target_date.strftime("%Y-%m-%d"))
                target_date += timedelta(days=7)  # 한 주 뒤의 같은 요일로 이동

        return dates

    @transaction.atomic
    def post(self, request):
        data = request.POST
        # 현재 작성하는 사람의 세션을 가져옴
        # member = request.session['member']

        # 강의 구분
        print(data['product-index'])
        # 식물 종류
        plants = data.getlist('plant-type')
        for key in plants:
            print(key)
        # 가격
        print(int(data['price-input']))
        # 인원
        print(int(data['member-input']))

        # 날짜, 시간 넣기
        start_date_input = data['start-date-input']
        end_date_input = data['end-date-input']
        weekday_type = data['weekday-type']

        # 날짜 범위 및 요일 유형을 기반으로 날짜 리스트 가져오기
        dates = self.date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # 계산된 날짜를 출력
        print(dates)

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        print(data['start-time-input'])
        print(data['end-time-input'])
        print(data['time-type'])
        # Diy키드 넣기
        name1 = data['diy-name-input1']
        content1 = data['diy-content-input1']
        print(name1, content1)
        name2 = data['diy-name-input2']
        content2 = data['diy-content-input2']
        print(name2, content2)

        # 제목 넣기
        print(data['title-input'])

        # 내용 넣기
        print(data['content-text-area'])

        # 사진넣기

        # for key in file:
        #     PostFile.objects.create(post=post, path=file[key])

        return redirect('lecture:detail-online')

class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


