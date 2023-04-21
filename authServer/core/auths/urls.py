from django.urls import path
from .views import (
    RegisterView,
    CheckInfoView,
    GetMoreInfoView,
    createLastLogin,
#     RetrieveUserView,
#     CheckEmailView,
#     LastLoginView
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('check', CheckInfoView.as_view()),
    path('getmorelogininfo', GetMoreInfoView.as_view()),
    path('lastlogin', createLastLogin.as_view()),
    # path('check_email', CheckEmailView.as_view()),
    # path('lastlogin', LastLoginView.as_view()),

    # app v1
    # path('v1/validate-licensekey', checkLicenseKey.as_view()),
    # path('v1/licensekey', LicenseKey.as_view()),
]