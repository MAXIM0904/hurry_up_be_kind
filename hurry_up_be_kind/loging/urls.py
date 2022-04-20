from django.urls import path
from .views import UserInfToken, RegistrationUser, Loging, Logout, UserUpdateProfile, UserDelete

app_name = 'logging/'

urlpatterns = [
    path('registration_user/', RegistrationUser.as_view(), name='registration_user'),
    path('inf_user/', UserInfToken.as_view(), name='inf_user'),
    path('logging/', Loging.as_view(), name='loging'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user_update_profile/', UserUpdateProfile.as_view(), name='user_update_profile'),
    path('user_delete/', UserDelete.as_view(), name='user_delete')
]
