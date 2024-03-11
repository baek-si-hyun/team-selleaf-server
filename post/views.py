from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from post.models import Post, PostCategory, PostTag, PostPlant, PostFile


# Create your views here.
class PostCreateView(View):
    def get(self, request):
        return render(request, 'community/web/post/create-post.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        files = request.FILES

        print(data)

        # 현재 로그인된 사람의 정보
        member = Member(**request.session['member'])

        # 포스트
        post = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }

        post_data = Post.objects.create(**post)

        # 카테고리
        post_category = {
            'category_name': data['post-category'],
            'post': post_data
        }

        PostCategory.objects.create(**post_category)

        # 포스트 태그
        post_tag = {
            'tag_name': data['post-tags'],
            'post': post_data
        }

        PostTag.objects.create(**post_tag)

        plant_types = data.getlist('plant-type')

        # 식물 종류
        for plant_type in plant_types:
            # print(plant_type)
            PostPlant.objects.create(post=post_data, plant_name=plant_type)

        # 첨부파일
        for key in files:
            # print(key)
            PostFile.objects.create(post=post_data, file_url=files[key])
        return redirect(f'/post/detail/?id={post_data.id}')

class PostDetailView(View):
    def get(self):
        pass