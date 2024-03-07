from django.db import transaction
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View

from member.models import Member
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


class TradeMainView(View):
    def get(self, request):
        return render(request, "trade/web/trade-main.html")

class TradeTotalView(View):
    def get(self, request):
        return render(request, "trade/web/trade-total.html")

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