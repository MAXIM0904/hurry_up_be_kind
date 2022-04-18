from django.urls import path, re_path
from .views import UserInfToken, RegistrationUser

app_name = 'loging/'

urlpatterns = [
    path('registration_user/', RegistrationUser.as_view(), name='registration_user'),
    path('inf_user/', UserInfToken.as_view(), name='inf_user'),
    path('logout/', Logo.as_view(), name='inf_user'),
]
