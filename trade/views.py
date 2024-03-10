from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, MemberProfile, MemberAddress
from plant.models import Plant
from trade.models import TradeCategory, Trade, TradeFile, TradePlant


class TradeDetailView(View):
    def get(self, request):

        # upload 페이지에서 사용자가 올린 거래 게시물이 detail 화면에서 보여줘야 하기 때문에 trade 가져옴
        # 방금 올린 거래 게시물
        trade = Trade.objects.get(id=request.GET['id'])

        # 방금 올린 거래 게시물을 작성한 사용자 찾기
        member_search_trade = Trade.objects.filter(id=request.GET['id']).values('member_id').first()

        # 방금 거래 게시물을 올린 사용자가 작성한 다른 거래 게시물
        trades = Trade.objects.filter(member=member_search_trade['member_id'], status=True).values()

        for td in trades:
            product_img = TradeFile.objects.filter(trade_id=td['id']).values('file_url').first()
            td['product_img'] = product_img['file_url']
            product_plants = TradePlant.objects.filter(trade_id=td['id']).values('plant_name')
            product_plants_list = list(product_plants)

            product_list = [item['plant_name'] for item in product_plants_list]
            td['plant_name'] = product_list

        context = {
            'trade': trade,
            'trade_files': list(trade.tradefile_set.all()),
            'trade_file': list(trade.tradefile_set.all())[0],
            'trades': trades,
        }

        return render(request, "trade/web/trade-detail.html", context)

class TradeUpdateView(View):
    def get(self, request):
        trade = Trade.objects.get(id=request.GET['id'])
        return render(request, "trade/web/trade-update.html", {'trade': trade})

    @transaction.atomic
    def post(self, request):
        data = request.POST
        trade_id = data['id']

        # 수정할 거래 게시물 가져오기
        trade = Trade.objects.get(id=trade_id)

        # # 게시물중 카테고리 아이디 찾아오기
        # trade_category_number = Trade.objects.filter(id=trade_id).values('trade_category_id')
        trade_category_number = Trade.objects.get(id=trade_id).trade_category_id

        # 게시물 상품 구분 수정
        trade_category = TradeCategory.objects.get(id=trade_category_number)
        trade_category.category_name = data['product-index']

        # 게시물 식물 종류 수정
        trade_plants = TradePlant.objects.filter(trade_id=trade_id).delete()
        plant_types = data.getlist('plant-type')
        for plant_type in plant_types:
            TradePlant.objects.create(trade=trade, plant_name=plant_type)

        # 게시물 가격 수정
        trade.trade_price = data['price-input']

        # 게시물 오픈채팅방 링크 수정
        trade.kakao_talk_url = data['chatting-input']

        # 게시물 제목 수정
        trade.trade_title = data['title-input']

        # 게시물 내용 수정
        trade.trade_content = data['content-input']

        # 게시물 update
        trade.save(update_fields=['trade_price', 'kakao_talk_url', 'trade_title', 'trade_content'])

        # 카테고리 update
        trade_category.save(update_fields=['category_name'])

        return redirect(f'/trade/detail/?id={trade.id}')

class TradeDeleteView(View):
    def get(self, request):
        Trade.objects.filter(id=request.GET['id']).update(status=False)

        return redirect('/trade/total')

class TradeMainView(View):
    def get(self, request):

        # 현재 로그인한 사용자 정보 가져오기
        member = request.session['member']

        # 로그인한 사용자의 주소를 찾아오기( 주변 상품을 뿌려줄 때 사용해야 하기 때문 )
        member_home = MemberAddress.objects.filter(member_id=member['id']).values('address_city', 'address_district').first()

        # member_address 테이블에서 현재 로그인한 사용자와 같은 주소에 사는 사람들을 먼저 찾기
        local_persons = MemberAddress.objects.filter(address_city=member_home['address_city'], address_district=member_home['address_district']).values('member_id')

        # 위의 local_persons가 현재 로그인한 사용자와 같은 지역에 사는 사람들임(자기 포함)
        # 이제 이걸 가지고 local_persons가 쓴 거래 게시물을 찾아서 뿌려주면 끝!
        local_person_list = []
        for local_person in local_persons:
            local_person_list.append(local_person['member_id'])


        trades = Trade.objects.filter(status=True, member_id__in=local_person_list).annotate(member_name=F('member__member_name')) \
            .values('trade_title', 'trade_price', 'member_name', 'id', 'member_id')

        for trade in trades:
            trade_file = TradeFile.objects.filter(trade_id=trade['id']).values('file_url').first()
            profile = MemberProfile.objects.filter(member_id=trade['member_id']).values('file_url').first()
            trade['trade_file'] = trade_file['file_url']
            trade['profile'] = profile['file_url']

            product_plants = TradePlant.objects.filter(trade_id=trade['id']).values('plant_name')
            product_plants_list = list(product_plants)

            product_list = [item['plant_name'] for item in product_plants_list]
            trade['plant_name'] = product_list

        context ={
            'trades': trades,
            'member_home': member_home,
        }
        return render(request, "trade/web/trade-main.html", context)

class TradeTotalView(View):
    def get(self, request):
        return render(request, "trade/web/trade-total.html")

class TradeTotalApi(APIView):
    def get(self, request, page):
        row_count = 8
        offset = (page - 1) * row_count
        limit = row_count * page


        trades = Trade.objects.filter(status=True).annotate(member_name=F('member__member_name'))\
            .values('trade_title', 'trade_price', 'member_name', 'id', 'member_id')

        for trade in trades:
            trade_file = TradeFile.objects.filter(trade_id=trade['id']).values('file_url').first()
            profile = MemberProfile.objects.filter(member_id=trade['member_id']).values('file_url').first()
            trade['trade_file'] = trade_file['file_url']
            trade['profile'] = profile['file_url']

            product_plants = TradePlant.objects.filter(trade_id=trade['id']).values('plant_name')
            product_plants_list = list(product_plants)

            product_list = [item['plant_name'] for item in product_plants_list]
            trade['plant_name'] = product_list

        return Response(trades[offset:limit])

class TradeUploadView(View):
    def get(self, request):
        member = request.session['member']
        return render(request, "trade/web/trade-upload.html")

    @transaction.atomic
    def post(self, request):
        trade_data = request.POST
        files = request.FILES

        # 현재 로그인한 사용자
        member = request.session['member']


        # 상품 구분
        # trade_data['product-index']

        # 식물 종류
        # trade_data.getlist('plant-type')

        # 가격
        # trade_data['price-input']

        # 오픈 채팅방 링크
        # trade_data['chatting-input']

        # 거래 게시글 제목
        # trade_data['title-input']

        # 거래 게시글 내용
        # trade_data['content-input']

        # Trade create
        data = {
            'trade_price': trade_data['price-input'],
            'trade_title': trade_data['title-input'],
            'trade_content': trade_data['content-input'],
            'member': Member.objects.get(id=member['id']),
            'trade_category': TradeCategory.objects.create(category_name=trade_data['product-index']),
            'kakao_talk_url': trade_data['chatting-input'],
        }

        trade = Trade.objects.create(**data)

        # TradeFile create
        for key in files:
            TradeFile.objects.create(trade=trade, file_url=files[key])

        # TradePlant create
        plant_types = trade_data.getlist('plant-type')
        for plant_type in plant_types:
            TradePlant.objects.create(trade=trade, plant_name=plant_type)

        return redirect(f'/trade/detail/?id={trade.id}')