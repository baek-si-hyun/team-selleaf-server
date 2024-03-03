from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView


class MainView(View):
    def get(self, request):
        return render(request, 'main/main.html')

class MainKnowhowAPI(APIView):
    pass