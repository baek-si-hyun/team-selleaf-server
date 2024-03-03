from django.shortcuts import render
from django.views import View


class AlarmView(View):
    def get(self, request):
        return render(request,'alarm/alarm.html')