from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View

from plant.models import Plant


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
        member = request.session['member']
        print(member)
        print(trade_data['product-index'])
        print(trade_data.getlist('plant-type'))
        plant = {
            'plant_name': trade_data.getlist('plant-type')
        }
        # plant = Plant.objects.get(id=1)
        # print(type(plant.plant_name))
        # trade_data = {
        #     ''
        # }

        return redirect('trade:detail')