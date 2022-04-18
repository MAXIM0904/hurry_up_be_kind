from .views import AllPhilantropistListView
from django.urls import path

urlpatterns = [
    path('', AllPhilantropistListView.as_view(), name='all_philantropist'),
]