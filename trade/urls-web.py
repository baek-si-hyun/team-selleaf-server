from django.urls import path

from trade.views import TradeMainView, TradeDetailView, TradeTotalView, TradeUploadView, TradeUpdateView, \
    TradeDeleteView, TradeTotalApi

app_name = 'trade'

urlpatterns = [
    # 거래 게시물 상세 페이지
    path('detail/', TradeDetailView.as_view(), name='detail'),

    # 거래 게시물 수정 페이지
    path('update/', TradeUpdateView.as_view(), name='update'),

    # 거래 게시물 삭제 페이지
    path('delete/', TradeDeleteView.as_view(), name='delete'),

    # 거래 게시물 메인 페이지
    path('main/', TradeMainView.as_view(), name='main'),

    # 전체 거래 게시물 보기 페이지
    path('total/', TradeTotalView.as_view(), name='total'),
    path('total/<int:page>', TradeTotalApi.as_view(), name='total'),

    # 거래 게시물 작성 페이지
    path('upload/', TradeUploadView.as_view(), name='upload'),
]
