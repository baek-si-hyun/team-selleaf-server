import random

from django.test import TestCase

from member.models import Member
from post.models import Post


class PostTest(TestCase):


    member_queryset = Member.objects.all()

    for i in range(50):
        post = {
            'post_title': f'게시물 제목{i}',
            'post_content': f'게시물 내용{i}',
            'member': member_queryset[random.randint(0, len(member_queryset)-1)],
        }
        Post.objects.create(**post)

