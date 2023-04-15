from django.urls import path
from .views import (
    RegisterView,
    # RetrieveUserView,
    # CheckEmailView,
    # LastLoginView
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    # path('me', RetrieveUserView.as_view()),
    # path('check_email', CheckEmailView.as_view()),
    # path('lastlogin', LastLoginView.as_view()),
]