from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login')
]

