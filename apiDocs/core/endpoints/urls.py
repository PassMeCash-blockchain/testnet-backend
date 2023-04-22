from django.urls import path
from .views import (
    RegisterView,
    PersonalView,
    ContactView,LoginView,
)

urlpatterns = [
    # PassMeCash API Documentation
    path('create', RegisterView.as_view()),
    path('personal-info', PersonalView.as_view()),
    path('contact-info', ContactView.as_view()),
    path('login', LoginView.as_view()),
]