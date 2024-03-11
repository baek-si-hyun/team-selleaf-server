from datetime import datetime, timedelta

from django.db import transaction
from django.db.models import Count, Avg, Sum
from django.shortcuts import render, redirect
from django.views import View

from lecture.models import LectureCategory, Lecture, LectureProductFile, LecturePlant, Kit, LectureReview, \
    LectureAddress
from member.models import Member
from selleaf.date import Date
from selleaf.time import Time
from teacher.models import Teacher

def date_range_with_weekdays(start, end, weekday_type):
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

def divide_time_intervals(start_time, end_time, interval):
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


class LectureView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-main.html')


class LectureDetailOnlineView(View):
    def get(self, request):
        lecture = Lecture.objects.get(id=request.GET['id'], online_status=True)
        date = Date.objects.filter(lecture_id=request.GET['id']).first()
        # print(lecture)

        review_count = LectureReview.objects.filter(lecture_id=request.GET['id']).count()
        # print(review_count)

        # 방금 올린 강의를 작성한 사용자 찾기
        teacher_id = lecture.teacher_id
        # print(teacher_id)

        # 해당 강의에 대한 별점에 따른 리뷰 개수
        rating_counts = LectureReview.objects.filter(lecture_id=request.GET['id']).values('review_rating').annotate(
            count=Count('id'))

        # 별점 범위와 개수
        rating_dict = {str(i): 0 for i in range(1, 6)}

        # 각 별점에 따른 개수 저장
        for item in rating_counts:
            rating_dict[str(item['review_rating'])] = item['count']
        # print(rating_dict)

        # 리뷰 평균 구하기
            # 해당 강의에 대한 리뷰들의 총합과 개수를 구함
        review_sum = LectureReview.objects.filter(lecture_id=request.GET['id']).aggregate(sum_rating=Sum('review_rating'),
                                                                                   count=Count('id'))

        # 리뷰가 있는 경우에만 평균을 계산
        if review_sum['count'] > 0:
            average_rating = round(review_sum['sum_rating'] / review_sum['count'], 1)
        else:
            average_rating = 0

        # print(average_rating)

        # 방금 강의를 올린 사용자가 작성한 다른 강의
        lectures = Lecture.objects.filter(teacher_id=teacher_id, lecture_status=True).values()
        # print(lectures)

        for lte in lectures:
            lecture_img = LectureProductFile.objects.filter(lecture_id=lte['id']).values('file_url').first()

            if lecture_img:
                lte['product_img'] = lecture_img['file_url']
            else:
                # 기본값이나 스킵 처리 등을 추가할 수 있음
                lte['product_img'] = None  # 혹은 기본 이미지 URL 설정

            lecture_plants = LecturePlant.objects.filter(lecture_id=lte['id']).values('plant_name')
            lecture_plants_list = list(lecture_plants)
            product_list = [item['plant_name'] for item in lecture_plants_list]
            lte['plant_name'] = product_list

        dates = lecture.date_set.all()
        times = date.time_set.all()
        kits = lecture.kit_set.all()
        reviews = lecture.lecturereview_set.all()
        # print(reviews)

        context = {
            'lecture': lecture,
            'lecture_files': list(lecture.lectureproductfile_set.all()),
            'lecture_file': list(lecture.lectureproductfile_set.all())[0],
            'lecture_order_date': dates.order_by('date'),
            'lecture_order_time': times.order_by('time'),
            'lecture_kit': kits.all(),
            'reviews': reviews,
            'lectures': lectures,
            'review_count': review_count,
            'rating_counts': rating_dict,
            'average_rating': average_rating
        }

        return render(request, 'lecture/web/lecture-detail-online.html', context)



class LectureDetailOfflineView(View):
    def get(self, request):
        lecture = Lecture.objects.get(id=request.GET['id'], online_status=False)
        date = Date.objects.filter(lecture_id=request.GET['id']).first()
        # print(lecture)

        review_count = LectureReview.objects.filter(lecture_id=request.GET['id']).count()
        # print(review_count)

        # 방금 올린 강의를 작성한 사용자 찾기
        teacher_id = lecture.teacher_id
        # print(teacher_id)

        # 해당 강의에 대한 별점에 따른 리뷰 개수
        rating_counts = LectureReview.objects.filter(lecture_id=request.GET['id']).values('review_rating').annotate(
            count=Count('id'))

        # 별점 범위와 개수
        rating_dict = {str(i): 0 for i in range(1, 6)}

        # 각 별점에 따른 개수 저장
        for item in rating_counts:
            rating_dict[str(item['review_rating'])] = item['count']
        # print(rating_dict)

        # 리뷰 평균 구하기
        # 해당 강의에 대한 리뷰들의 총합과 개수를 구함
        review_sum = LectureReview.objects.filter(lecture_id=request.GET['id']).aggregate(
            sum_rating=Sum('review_rating'),
            count=Count('id'))

        # 리뷰가 있는 경우에만 평균을 계산
        if review_sum['count'] > 0:
            average_rating = round(review_sum['sum_rating'] / review_sum['count'], 1)
        else:
            average_rating = 0

        print(average_rating)

        # 방금 강의를 올린 사용자가 작성한 다른 강의
        lectures = Lecture.objects.filter(teacher_id=teacher_id, lecture_status=True).values()
        # print(lectures)

        for lte in lectures:
            lecture_img = LectureProductFile.objects.filter(lecture_id=lte['id']).values('file_url').first()

            if lecture_img:
                lte['product_img'] = lecture_img['file_url']
            else:
                # 기본값이나 스킵 처리 등을 추가할 수 있음
                lte['product_img'] = None  # 혹은 기본 이미지 URL 설정

            lecture_plants = LecturePlant.objects.filter(lecture_id=lte['id']).values('plant_name')
            lecture_plants_list = list(lecture_plants)
            product_list = [item['plant_name'] for item in lecture_plants_list]
            lte['plant_name'] = product_list

        dates = lecture.date_set.all()
        times = date.time_set.all()
        reviews = lecture.lecturereview_set.all()
        address = lecture.lectureaddress_set.first()
        print(address)
        # print(reviews)

        context = {
            'lecture': lecture,
            'lecture_files': list(lecture.lectureproductfile_set.all()),
            'lecture_file': list(lecture.lectureproductfile_set.all())[0],
            'lecture_order_date': dates.order_by('date'),
            'lecture_order_time': times.order_by('time'),
            'reviews': reviews,
            'address': address,
            'lectures': lectures,
            'review_count': review_count,
            'rating_counts': rating_dict,
            'average_rating': average_rating
        }

        return render(request, 'lecture/web/lecture-detail-offline.html', context)




class LectureTotalView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-total.html')


class LectureUploadOnlineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-online.html')

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
            'online_status': True,
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
        dates = date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        start_time = request.POST.get('start-time-input')
        end_time = request.POST.get('end-time-input')
        interval = request.POST.get('time-type')

        # 시간대를 나누고 남은 시간을 추가하여 출력
        time_intervals = divide_time_intervals(start_time, end_time, interval)

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
        diy_name_input = request.POST.getlist('diy-name-input')
        diy_content_input = request.POST.getlist('diy-content-input')
        for i in range(len(diy_name_input)):
            Kit.objects.create(lecture=lecture, kit_name=diy_name_input[i], kit_content=diy_content_input[i])

        return redirect(f'/lecture/detail/online/?id={lecture.id}')

class LectureUploadOfflineView(View):
    def get(self, request):
        return render(request, 'lecture/web/lecture-upload-offline.html')


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
            'online_status': False,
        }
        # Lecture create
        lecture = Lecture.objects.create(**data)

        # LecturePlant create
        plant_types = lecture_data.getlist('plant-type')
        for plant_type in plant_types:
            LecturePlant.objects.create(lecture=lecture, plant_name=plant_type)

        # 강의 장소 넣어주기
        local_selected = request.POST.get('product-index-local')
        control_selected = request.POST.get('product-index-control')
        LectureAddress.objects.create(lecture=lecture, address_city=local_selected, address_district=control_selected, address_detail="입니다.")

        # 날짜, 시간 넣기
        start_date_input = request.POST.get('start-date-input')
        end_date_input = request.POST.get('end-date-input')
        weekday_type = request.POST.getlist('weekday-type')

        # 날짜 범위 및 요일 유형을 기반으로 날짜 리스트 가져오기
        dates = date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        start_time = request.POST.get('start-time-input')
        end_time = request.POST.get('end-time-input')
        interval = request.POST.get('time-type')

        # 시간대를 나누고 남은 시간을 추가하여 출력
        time_intervals = divide_time_intervals(start_time, end_time, interval)

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

        # LectureProductFile create
        for key in files:
            LectureProductFile.objects.create(lecture=lecture, file_url=files[key])



        return redirect(f'/lecture/detail/offline/?id={lecture.id}')


class LectureUpdateOnlineView(View):
    def get(self, request):
        lecture = Lecture.objects.get(id=request.GET['id'])
        kits = Kit.objects.filter(lecture_id=lecture.id).values()

        context = {
            'lecture': lecture,
            'kits' : kits
        }
        # print(lecture)

        return render(request, "lecture/web/lecture-update-online.html", context)

    @transaction.atomic
    def post(self, request):
        data = request.POST
        lecture_id = data['id']

        # 수정할 게시물 가져오기
        lecture = Lecture.objects.get(id=lecture_id)

        # 게시물 중 카테고리 아이디 찾아오기
        lecture_category_number = Lecture.objects.get(id=lecture_id).lecture_category_id

        # 게시물 강의 구분 수정
        lecture_category = LectureCategory.objects.get(id=lecture_category_number)
        lecture_category.category_name = data['product-index']

        # 게시물 식물 종류 수정
        LecturePlant.objects.filter(lecture_id=lecture_id).delete()
        plant_types = data.getlist('plant-type')
        for plant_type in plant_types:
            LecturePlant.objects.create(lecture=lecture, plant_name=plant_type)

        # 현재 강의에서 Date id 찾아오기
        deleteDates = Date.objects.filter(lecture_id=lecture.id).values('id')
        deleteDateList = []
        for deleteDate in deleteDates:
            deleteDateList.append(deleteDate['id'])

        # 현재 강의에서 날짜를 통해 시간 찾아와서 삭제해주기
        deleteTime = Time.objects.filter(date_id__in=deleteDateList).delete()

        # 현재 강의에서 날짜를 찾아 해당 날짜들 삭제해주기
        realDeleteDate = Date.objects.filter(lecture_id=lecture.id).delete()

        # kit 수정
        diy_name_inputs = request.POST.getlist('diy-name-input')
        diy_content_inputs = request.POST.getlist('diy-content-input')

        kits = Kit.objects.filter(lecture_id=lecture.id)
        # kits[0].kit_name = diy_name_inputs[0]
        # kits[0].kit_content = diy_content_inputs[0]
        # kits[0].save(update_fields=['kit_name', 'kit_content'])
        # kits[1].kit_name = diy_name_inputs[1]
        # kits[1].kit_content = diy_content_inputs[1]
        # kits[1].save(update_fields=['kit_name', 'kit_content'])
        for i, kit in enumerate(kits):
            if i < len(diy_name_inputs):
                kit.kit_name = diy_name_inputs[i]
            if i < len(diy_content_inputs):
                kit.kit_content = diy_content_inputs[i]
            kit.save(update_fields=['kit_name', 'kit_content'])

        # # 날짜 정보 수정
        start_date_input = data.get('start-date-input')
        end_date_input = data.get('end-date-input')
        weekday_type = data.getlist('weekday-type')


        # 날짜 범위 및 요일 유형을 기반으로 날짜 리스트 가져오기
        dates = date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # # 삭제할 강의를 찾고 그 시간을 없애주면 됨

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        start_time = data.get('start-time-input')
        end_time = data.get('end-time-input')
        interval = data.get('time-type')

        # 시간대를 나누고 남은 시간을 추가하여 출력
        time_intervals = divide_time_intervals(start_time, end_time, interval)

        times = []
        # 계산된 시간대를 출력
        for interval in time_intervals:
            times.append(f"{interval[0]}~{interval[1]}")

        # 날짜 및 시간 데이터 생성
        for date in dates:
            lecture_date = Date.objects.create(lecture=lecture, date=date)
            for time in times:
                Time.objects.create(date=lecture_date, time=time)

        # 게시물 가격 수정
        lecture.lecture_price = data['price-input']
        # 게시물 인원 수정
        lecture.lecture_headcount = data['number-input']
        # 게시물 제목 수정
        lecture.lecture_title = data['title-input']
        # 게시물 내용 수정
        lecture.lecture_content = data['content-text-area']

        # 게시물 및 카테고리 정보 저장
        lecture.save(update_fields=['lecture_price', 'lecture_headcount', 'lecture_title', 'lecture_content'])
        lecture_category.save(update_fields=['lecture_category_name'])

        return redirect(f'/lecture/detail/online?id={lecture.id}')


class LectureUpdateOfflineView(View):
    def get(self, request):
        lecture = Lecture.objects.get(id=request.GET['id'])
        context = {
            'lecture': lecture,
        }
        # print(lecture)

        return render(request, "lecture/web/lecture-update-offline.html", context)

    @transaction.atomic
    def post(self, request):
        data = request.POST
        lecture_id = data['id']

        # 수정할 게시물 가져오기
        lecture = Lecture.objects.get(id=lecture_id)

        # 게시물 중 카테고리 아이디 찾아오기
        lecture_category_number = Lecture.objects.get(id=lecture_id).lecture_category_id

        # 게시물 강의 구분 수정
        lecture_category = LectureCategory.objects.get(id=lecture_category_number)
        lecture_category.category_name = data['product-index']

        # 게시물 중 강의 지역 가져오기

        # 게시물 식물 종류 수정
        lecture_plants = LecturePlant.objects.filter(lecture_id=lecture_id).delete()
        plant_types = data.getlist('plant_type')
        for plant_type in plant_types:
            LecturePlant.objects.create(lecture=lecture, plant_name=plant_type)

        # 날짜 정보 수정
        start_date_input = data.get('start-date-input')
        end_date_input = data.get('end-date-input')
        weekday_type = data.getlist('weekday-type')

        # 날짜 및 시간 데이터 삭제
        # lecture.date_set.all().delete()
        print(lecture.date_set.all())

        # 날짜 범위 및 요일 유형을 기반으로 날짜 리스트 가져오기
        dates = date_range_with_weekdays(start_date_input, end_date_input, weekday_type)

        # 강의 시간(시작 시간, 종료 시간, 강의 시간)
        start_time = data.get('start-time-input')
        end_time = data.get('end-time-input')
        interval = data.get('time-type')

        # 시간대를 나누고 남은 시간을 추가하여 출력
        time_intervals = divide_time_intervals(start_time, end_time, interval)

        times = []
        # 계산된 시간대를 출력
        for interval in time_intervals:
            times.append(f"{interval[0]}~{interval[1]}")

        # 날짜 및 시간 데이터 생성
        for date in dates:
            lecture_date = Date.objects.create(lecture=lecture, date=date)
            for time in times:
                Time.objects.create(date=lecture_date, time=time)


        # 게시물 가격 수정
        lecture.lecture_price = data['price-input']
        # 게시물 인원 수정
        lecture.lecture_headcount = data['number-input']
        # 게시물 제목 수정
        lecture.lecture_title = data['title-input']
        # 게시물 내용 수정
        lecture.lecture_content = data['content-input']

        # 게시물 update
        lecture.save(update_fields=['lecture_price', 'lecture_headcount', 'lecture_title', 'lecture_content'])

        # 카테고리 update
        lecture_category.save(update_fields=['category_name'])

        return redirect(f'/lecture/detail/offline?id={lecture.id}')

class LectureDeleteView(View):
    def get(self, request):
        Lecture.objects.filter(id=request.GET['id']).update(lecture_status=True)

        return redirect('/lecture/total')
