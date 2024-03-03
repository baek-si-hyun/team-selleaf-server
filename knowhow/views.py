from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from knowhow.models import Knowhow, KnowhowFile
from member.models import Member


class KnowhowCreateView(View):
    def get(self, request):
        return render(request, 'community/web/knowhow/create-knowhow.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        # input 태그 하나 당 파일 1개일 때
        file = request.FILES

        # input 태그 하나에 여러 파일일 때(multiple), getlist('{input태그 name값}')
        # files = request.FILES.getlist('upload-file')

        member = Member(**request.session['member'])

        # knowhowcategory = {
        #
        # }


        knowhow = {
            'knowhow_title': data['knowhow-title'],
            'knowhow_content': data['knowhow-content'],
            'member': member
        }

        knowhowplant = {
            'plant_name': data['plant-name']
        }

        knowhowtag = {
            'tag_name': data['knowhow-tags']
        }




        knowhowdata = Knowhow.objects.create(**knowhow)

        # for file in files:
        #     KnowhowFile.objects.create(post=knowhowdata, path=file)

        for key in file:
            KnowhowFile.objects.create(post=knowhowdata, path=file[key])

        return redirect(post.get_absolute_url())
class KnowhowDetailView(View):
    pass

class KnowhowListView(View):
    pass