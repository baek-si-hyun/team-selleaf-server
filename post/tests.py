import random

from django.test import TestCase

from member.models import Member
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from post.models import Post, PostFile


class PostTest(TestCase):
    member_queryset = Member.objects.all()
    # for i in range(20):
    #     post_data = {
    #         'post_title': f'게시물 제목{i}',
    #         'post_content': f'게시물 내용{i}',
    #         'member': member_queryset[random.randint(ids)],
    #     }
    #     post = Post.objects.create(**post_data)
    #
    #     # PostFile 생성
    #     post_file_data = {
    #         'post': post,
    #         'file_url': 'https://imagedelivery.net/4aEUbX05h6IovGOQjgkfSw/88ed654b-a983-4019-dff7-921f0c15d700/public'
    #     }
    #     PostFile.objects.create(**post_file_data)
    #

    print(random.choice(member_queryset.values('id')))

    ids = member_queryset.values_list('id', flat=True)

    for number in range(1, 10):

        response = urlopen('https://www.gardening.news/news/articleView.html?idxno=' + str(number))
        soup = BeautifulSoup(response, 'html.parser')

        title_list = soup.select('h1', {'class': 'heading'})
        if title_list:
            title = title_list[0].text.strip()
        else:
            title = ''

        content_list = soup.select('p')
        if content_list:
            content = content_list[0].text.strip()
        else:
            content = ''

        img_list = soup.find('img')
        if img_list and 'src' in img_list.attrs:
            img_src = img_list['src']  # Get the value of the src attribute
        else:
            img_src = ''

        post_data = {
            'post_title': title,
            'post_content': content,
            'member': random.choice(member_queryset),
        }
        post = Post.objects.create(**post_data)
