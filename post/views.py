from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member, MemberProfile
from post.models import Post, PostCategory, PostTag, PostPlant, PostFile, PostReply


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
    def get(self, request):
        post = Post.objects.get(id=request.GET['id'])
        post_tags = PostTag.objects.filter(post_id__gte=1).values('tag_name')
        reply_count = PostReply.objects.filter(post_id=post.id).values('id').count()
        member_profile = MemberProfile.objects.filter(id=post.member_id).values('file_url')
        post_category = PostCategory.objects.filter(post_id=post).values('category_name').first()
        post_plant = PostPlant.objects.filter(post_id=post.id).values('plant_name')

        post.post_count += 1
        post.save(update_fields=['post_count'])

        post_files = list(post.postfile_set.all())
        post_file = list(post.postfile_set.all())[0]

        context = {
            'post': post,
            'post_files': post_files,
            'post_file': post_file,
            'post_tags': post_tags,
            'reply_count': reply_count,
            'member_profile': member_profile,
            'post_category': post_category,
            'post_plant': post_plant
        }

        return render(request, 'community/web/post/post-detail.html', context)