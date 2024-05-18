from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),  # Redirect root URL to the API endpoints
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
