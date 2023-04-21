from django.urls import path
from .views import (
    RegisterView,
    RegisterPersonalView,
    RegisterContactView,
    # RetrieveUserView,
    LoginView,
    # CheckEmailView,
    # LastLoginView
)

urlpatterns = [
    path('create', RegisterView.as_view()),
    path('personal-info', RegisterPersonalView.as_view()),
    path('contact-info', RegisterContactView.as_view()),
    path('login', LoginView.as_view()),
    # path('user', RetrieveUserView.as_view()),
    # path('check_email', CheckEmailView.as_view()),
    # path('lastlogin', LastLoginView.as_view()),
]