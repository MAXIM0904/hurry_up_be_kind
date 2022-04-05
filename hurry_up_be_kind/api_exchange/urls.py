from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList


app_name = 'api_exchange/'

urlpatterns = [
    path('all_philantropist', SnippetList.as_view(), name='all_philantropist')
]

urlpatterns = format_suffix_patterns(urlpatterns)