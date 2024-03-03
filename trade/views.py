from django.shortcuts import render
from django.views import View


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
        return render(request, "trade/web/trade-upload.html")