from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('_/', admin.site.urls),
    path('otp/v1/',include('service.urls'))
]
