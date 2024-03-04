from django.urls import path

from trade.views import TradeMainView, TradeDetailView, TradeTotalView, TradeUploadView

app_name = 'trade'

urlpatterns = [
    path('detail/', TradeDetailView.as_view(), name='detail'),
    path('main/', TradeMainView.as_view(), name='main'),
    path('total/', TradeTotalView.as_view(), name='total'),
    path('upload/', TradeUploadView.as_view(), name='upload'),
]
