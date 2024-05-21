import csv
import os
import pickle
from pathlib import Path
import joblib
from django.test import TestCase


from ai.models import AiPostReply
from member.models import Member
from post.models import Post


class AiTest(TestCase):
    pass

    # with open(os.path.join(Path(__file__).resolve().parent, 'ai/merge_comments_data.csv'), mode='r',
    #           encoding='utf-8-sig') as file:
    #     csv_reader = csv.DictReader(file)
    #     datas = [row for row in csv_reader]
    #
    # for data in datas:
    #     reply_data = {
    #         'comment': data['Comment'],
    #         'target': data['Target'],
    #     }
    #     AiPostReply.objects.create(**reply_data)

    # # 'model.pkl' 파일을 로드
    loaded_model = joblib.load(os.path.join(Path(__file__).resolve().parent, 'ai/commentai.pkl'))
    print(loaded_model)