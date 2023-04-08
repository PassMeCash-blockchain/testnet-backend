from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CSS)
admin.site.register(PdfFile)
admin.site.register(ImageFile)
admin.site.register(JSFile)
