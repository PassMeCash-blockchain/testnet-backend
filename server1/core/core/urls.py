from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('_/', admin.site.urls),
    
    # endpoints
    path('endpoint/v1/', include('endpoints.urls')),
]
