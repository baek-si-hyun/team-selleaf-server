from django.urls import path

from trade.views import TradeMainView, TradeDetailView, TradeTotalView, TradeUploadView, TradeUpdateView

app_name = 'trade'

urlpatterns = [
    path('detail/', TradeDetailView.as_view(), name='detail'),
    path('update/', TradeUpdateView.as_view(), name='update'),
    path('main/', TradeMainView.as_view(), name='main'),
    path('total/', TradeTotalView.as_view(), name='total'),
    path('upload/', TradeUploadView.as_view(), name='upload'),
]
