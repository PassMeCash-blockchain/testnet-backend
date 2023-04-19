from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="PassMeCash API",
      default_version='v1',
      description="Discription for PassMeCash Internal API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="api@passme.cash"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   #  path('_/', admin.site.urls),
    
    # endpoints
    path('endpoint/v1/', include('endpoints.urls')),

    # PassMeCash API Documentation
    path('docs/', include('djagger.urls')),
   #  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
