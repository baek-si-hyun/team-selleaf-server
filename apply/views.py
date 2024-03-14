from django.shortcuts import render
from django.views import View


class ApplyView(View):
    def post(self, request):
        return render(request, '')
