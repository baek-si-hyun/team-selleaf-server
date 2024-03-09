from django.urls import path

from qna.views import QnAListAPI

app_name = 'qna'

urlpatterns = [
    path('list/<int:page>/', QnAListAPI.as_view(), name='qna-list-api'),
]
