# rest_framework_simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('_/', admin.site.urls),

    # internal url
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),

    # endpoints
    path('auth/v1/', include('auths.urls')),

]
