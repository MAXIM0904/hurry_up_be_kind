from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_exchange/', include('api_exchange.urls')),
    path('', include('all_users.urls')),

]
