from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PhilantropistList, WardList


app_name = 'api_exchange/'

urlpatterns = [
    path('all_philantropist', PhilantropistList.as_view(), name='all_philantropist'),
    path('all_ward', WardList.as_view(), name='all_ward'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
