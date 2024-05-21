import csv
import os
import pickle
from pathlib import Path

from django.test import TestCase
import joblib

from member.models import Member


class AiTest(TestCase):
    # # 'model.pkl' 파일을 로드
    # loaded_model = joblib.load(os.path.join(Path(__file__).resolve().parent, 'ai/commentai.pkl'))
    #
    # # 로드된 모델을 사용
    # print(loaded_model)

    with open(os.path.join(Path(__file__).resolve().parent, 'ai/merge_comments_data.csv'), mode='r',
              encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        asd = [row for row in csv_reader]
        print(asd)

    for i in range(len(asd)):
        reply_data = {
            'comment': i.Comment,
            'target': i.Target,
        }
        print(reply_data)
