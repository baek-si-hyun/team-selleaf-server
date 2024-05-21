import csv
import os
import pickle
from pathlib import Path

from django.test import TestCase
import joblib

from ai.models import AiPostReply
from member.models import Member
from post.models import Post


class AiTest(TestCase):
    # # 'model.pkl' 파일을 로드
    # loaded_model = joblib.load(os.path.join(Path(__file__).resolve().parent, 'ai/commentai.pkl'))
    #
    # # 로드된 모델을 사용
    # print(loaded_model)

    with open(os.path.join(Path(__file__).resolve().parent, 'ai/merge_comments_data.csv'), mode='r',
              encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        asd = [{k: v.encode('utf-8').decode('utf-8-sig') if isinstance(v, str) else v for k, v in row.items()} for row in csv_reader]

    for i in asd:
        reply_data = {
            'comment': i['Comment'],
            'target': i['Target'],
        }
        # print(reply_data)
        AiPostReply.objects.create(**reply_data)
