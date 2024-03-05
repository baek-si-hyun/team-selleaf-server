from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View

from member.models import Member
from plant.models import Plant
from trade.models import TradeCategory, Trade, TradeFile


class TradeDetailView(View):
    def get(self, request):
        return render(request, "trade/web/trade-detail.html")

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

        # 사진파일
        # 거래게시물등록 서비스에서는 사진을 최대 5장까지 받을 수 있음
        # 하지만 1 ~ 5장까지 사용자가 몇장의 사진을 올렸는지는 모름 따라서
        # 나는 이를 반복문을 통해 해결하였음
        # realPhotos = []
        # photos = [trade_data['img-file1'], trade_data['img-file2'], trade_data['img-file3'], trade_data['img-file4'], trade_data['img-file5']]
        #
        # for photo in photos:
        #     if photo == '':
        #         continue
        #     realPhotos.append(photo)

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

        return redirect('trade:detail')