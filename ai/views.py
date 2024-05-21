from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from ai.models import AiPost


class PostAiAPIView(APIView):
    @staticmethod
    def get_index_from_title(title):
        return AiPost.objects.filter(title=title).values_list('id', flat=True).first()

    @staticmethod
    def get_title_from_index(index):
        return AiPost.objects.filter(id=index).values('post_title').first()

    @staticmethod
    def find_similar_titles(input_title, tfidf_matrix, vectorizer):
        input_vec = vectorizer.transform([input_title])
        cosine_similarities = cosine_similarity(input_vec, tfidf_matrix).flatten()
        return cosine_similarities

    @staticmethod
    def concatenate(features):
        return features['title'] + ' ' + features['content']

    @staticmethod
    def get_tag_from_index(index):
        tags = AiPost.objects.filter(id=index).values_list('post_tags', flat=True)
        if tags.exists():
            return tags.split(',')
        return '없습니다'

    def post(self, request):
        data = request.data

        # Concatenate features
        features = [self.concatenate(data)]

        count_v = CountVectorizer()
        count_metrix = count_v.fit_transform(features)

        c_s = cosine_similarity(count_metrix)
        # TF-IDF 벡터화
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(AiPost.objects.all().values_list('post_title', flat=True))

        # 실시간 입력 제목 예시
        input_title = features
        cosine_similarities = self.find_similar_titles(input_title, tfidf_matrix, vectorizer)

        # 유사도 높은 순으로 정렬
        similar_indices = cosine_similarities.argsort()[::-1]
        print(similar_indices)

        tag_set = set()
        # 결과 출력
        print("Input Title: ", input_title)
        print("Similar Titles and Recommended Tags:")
        for idx in similar_indices[1:6]:
            if cosine_similarities[idx] >= 0.1:
                row = AiPost.objects.filter(id = idx)
                print(f"Title: {row['post_title']}, Similarity: {cosine_similarities[idx]}")
                recommended_tag = sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1], reverse=True)
                for tag in recommended_tag[:3]:
                    tags = self.get_tag_from_index(tag[0])
                    tag_set.update(tags)

        # 결과 출력
        print("Recommended Tags:", tag_set)