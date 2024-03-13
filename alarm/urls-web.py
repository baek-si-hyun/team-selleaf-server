from django.urls import path

from alarm.views import AlarmView

app_name = 'alarm'

urlpatterns = [
    path('main/', AlarmView.as_view()),

]
