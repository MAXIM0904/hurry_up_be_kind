from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_exchange/', include('api_exchange.urls')),
    path('', include('all_users.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth_authtoken/', include('djoser.urls.authtoken')),
    path('auth/loging/', include('loging.urls')),
]
