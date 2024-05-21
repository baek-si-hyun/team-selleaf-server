from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ai.models import AiPost


# Create your views here.
class PostAiAPIView(APIView):
    @staticmethod
    def get_index_from_title(title):
        return AiPost.objects.filter(title=title).values_list('id', flat=True).first()

    @staticmethod
    def get_title_from_index(index):
        return AiPost.objects.filter(id=index).values('title').first()

    @staticmethod
    def get_tag_from_index(index):
        tags = AiPost.objects.filter(id=index).values_list('tag', flat=True)
        return list(tags)
    def post(self, request):
        data = request.data
        # def concatenate(features):
        #     return features['title'] + ' ' + features['content']

        # result_df = concatenate(data)

        count_v = CountVectorizer()
        count_metrix = count_v.fit_transform(data)
        c_s = cosine_similarity(count_metrix)

        title = data['title']
        index = self.get_index_from_title(title)
        title_check = self.get_title_from_index(index)
        print(title_check)
        recommended_tag = sorted(list(enumerate(c_s[index])), key=lambda x: x[1], reverse=True)
        tag_set = set()

        for tag in recommended_tag[1:4]:
            tags = self.get_tag_from_index(tag[0])
            tag_set.update(tags)

        return Response(tag_set)