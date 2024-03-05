from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView


class MainView(View):
    def get(self, request):
        member = request.session['member']
        profile = request.session['member_files'][0]
        print(profile)
        context = {
            'memberProfile': profile['file_url']
        }
        return render(request, 'main/main.html', context)


class MainKnowhowAPI(APIView):
    pass
