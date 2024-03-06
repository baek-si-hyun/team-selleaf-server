from datetime import datetime, timedelta

from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from lecture.models import LectureCategory, Lecture, LectureProductFile, LecturePlant, Kit
from member.models import Member
from selleaf.date import Date
from selleaf.time import Time
from teacher.models import Teacher


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')


class LectureDetailOnlineView(View):
    def get(self, request):
        lecture = Lecture.objects.get(id=request.GET['id'])
        # context = {
        #     'trade': trade,
        #     'trade_files': list(trade.tradefile_set.all()),
        #     'trade_file': list(trade.tradefile_set.all())[0]
        # }
        context = {
            'lecture': lecture,
            'lecture_files': list(lecture.lectureproductfile_set.all()),
            'lecture_file': list(lecture.lectureproductfile_set.all())[0],
            'lecture_order_date': lecture.date_set.all().order_by('date')
        }
        return render(request, 'lecture/web/lecture-detail-online.html', context)



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

    def divide_time_intervals(self, start_time, end_time, interval):
        # 시작 시간과 끝 시간을 datetime 객체로 변환
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")

        # 시간 간격을 분 단위로 변환
        interval_minutes = int(interval[:-3]) * 60

        # 결과를 저장할 리스트
        time_intervals = []

        # 시작 시간부터 끝 시간까지 시간 간격만큼씩 더해가며 시간대를 나눔
        while start + timedelta(minutes=interval_minutes) <= end:
            next_time = start + timedelta(minutes=interval_minutes)
            time_intervals.append((start.strftime("%H:%M"), next_time.strftime("%H:%M")))
            start = next_time

        # 남은 시간을 마지막에 추가
        if start < end:
            time_intervals.append((start.strftime("%H:%M"), end.strftime("%H:%M")))

        return time_intervals

    @transaction.atomic
    def post(self, request):
        lecture_data = request.POST
        files = request.FILES

        member = request.session['member']

        data = {
            'lecture_price': lecture_data['price-input'],
            'lecture_headcount': lecture_data['number-input'],
            'lecture_title': lecture_data['title-input'],
            'lecture_content': lecture_data['content-text-area'],
            'teacher': Teacher.objects.get(member_id=member['id']),
            'lecture_category': LectureCategory.objects.create(lecture_category_name=lecture_data['product-index']),
        }
        # Lecture create
        lecture = Lecture.objects.create(**data)

        # LecturePlant create
        plant_types = lecture_data.getlist('plant-type')
        for plant_type in plant_types:
            LecturePlant.objects.create(lecture=lecture, plant_name=plant_type)

        # 날짜, 시간 넣기
        start_date_input = request.POST.get('start-date-input')
        end_date_input = request.POST.get('end-date-input')
        weekday_type = request.POST.getlist('weekday-type')

        # 날짜 범위 및 요일 유형을 기반으로 날짜 리스트 가져오기
        dates = self.date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        start_time = request.POST.get('start-time-input')
        end_time = request.POST.get('end-time-input')
        interval = request.POST.get('time-type')

        # 시간대를 나누고 남은 시간을 추가하여 출력
        time_intervals = self.divide_time_intervals(start_time, end_time, interval)

        times = []
        # 계산된 시간대를 출력
        for interval in time_intervals:
            times.append(f"{interval[0]}~{interval[1]}")

        # 계산된 날짜를 출력
        # Date Create
        for date in dates:
            lecture_date = Date.objects.create(lecture=lecture, date=date)
            # Time Create

            for time in times:
                Time.objects.create(date=lecture_date, time=time)

        # # LectureProductFile create
        for key in files:
            LectureProductFile.objects.create(lecture=lecture, file_url=files[key])

        # Kit create
        diy_name_input =  request.POST.getlist('diy-name-input')
        diy_content_input = request.POST.getlist('diy-content-input')
        for i in range(len(diy_name_input)):
            Kit.objects.create(lecture=lecture, kit_name=diy_name_input[i], kit_content=diy_content_input[i])

        return redirect(f'/lecture/detail/online/?id={lecture.id}')

class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


