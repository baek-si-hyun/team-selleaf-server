from django.urls import path

from trade.views import TradeMainView, TradeDetailView, TradeTotalView, TradeUploadView, TradeUpdateView, \
    TradeDeleteView

app_name = 'trade'

urlpatterns = [
    path('detail/', TradeDetailView.as_view(), name='detail'),
    path('update/', TradeUpdateView.as_view(), name='update'),
    path('delete/', TradeDeleteView.as_view(), name='delete'),
    path('main/', TradeMainView.as_view(), name='main'),
    path('total/', TradeTotalView.as_view(), name='total'),
    path('total/<int:page>', TradeTotalView.as_view(), name='total'),
    path('upload/', TradeUploadView.as_view(), name='upload'),
]
