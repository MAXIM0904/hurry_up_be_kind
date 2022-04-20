from django.urls import path
from .views import UserInfToken, RegistrationUser, Loging, Logout

app_name = 'loging/'

urlpatterns = [
    path('registration_user/', RegistrationUser.as_view(), name='registration_user'),
    path('inf_user/', UserInfToken.as_view(), name='inf_user'),
    path('loging/', Loging.as_view(), name='loging'),
    path('logout/', Logout.as_view(), name='logout'),

]
