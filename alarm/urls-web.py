from django.urls import path

from alarm.views import AlarmView

app_name = 'alarm'

urlpatterns = [
    path('alarm',AlarmView.as_view(),name='alarm')
]
