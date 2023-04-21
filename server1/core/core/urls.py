from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    # endpoints
    path('endpoint/v1/', include('endpoints.urls')),

]
