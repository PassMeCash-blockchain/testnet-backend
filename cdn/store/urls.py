from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('upload/',Upload,name='upload'),
    path('assets/images/',GetAllImages,name='assetlink'),
    path('assets/images/<slug:slug>/',GetImageAssetUrl,name='imagelink'),
    path('assets/css/<slug:slug>/',GetCssAssetUrl,name='csslink'),
    path('assets/js/<slug:slug>/',GetJsAssetUrl,name='jslink'),
    path('assets/pdf/<slug:slug>/',GetPdfAssetUrl,name='pdflink'),

]
