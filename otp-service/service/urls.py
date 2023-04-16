from django.urls import path
from .views import *

urlpatterns = [
    path('create-or-update', createUpdateOtp.as_view()),
    path('verify', VerifyOtp.as_view()),
    path('reset', ResetOtp.as_view())
]

