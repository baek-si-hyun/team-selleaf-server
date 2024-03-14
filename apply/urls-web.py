from django.urls import path

from apply.views import ApplyOnlineView

app_name = 'apply'

urlpatterns = [
    path('', ApplyOnlineView.as_view(), name='apply'),

]
