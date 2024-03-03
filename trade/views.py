from django.shortcuts import render, redirect
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

    def post(self, request):
        request.session
        return redirect('trade:detail')