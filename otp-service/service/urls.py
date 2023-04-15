from django.urls import path
from .views import *
urlpatterns = [
    path('get-otp/',RequestOTP.as_view()),
    path('verify-otp/',VerifyOtp.as_view()),
    path('reset-otp/',ResetOTP.as_view())
]

